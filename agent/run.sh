#!/bin/bash
# traffic-intel 每日情报更新：抓榜单 → kimi 无头调研 → 校验 → 总览重建 → push（Actions 自动部署）
# crontab 示例：
#   23 6 * * * /usr/bin/flock -n /tmp/traffic-intel.lock /home/deploy/github/k3-test/traffic-intel/agent/run.sh >> /home/deploy/github/k3-test/traffic-intel/agent/update.log 2>&1
set -e
export PATH="/root/.kimi-code/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
cd "$(dirname "$(readlink -f "$0")")/.."   # 项目根 traffic-intel/

TODAY=$(date +%F)
STATE=agent/last_run
LAST_RUN=$(cat "$STATE" 2>/dev/null || date -d "yesterday" +%F)

echo "=== $(date '+%F %T') 开始更新（上次: $LAST_RUN） ==="

# 运行前快照 data/，用于事后对比是否有新内容
SNAP=$(mktemp -d)
cp data/products.json "$SNAP"/ 2>/dev/null || true

# 1. 抓取 traffic.cv 最新榜单，登记新域名
python3 agent/fetch_boards.py

# 2. 组装 prompt 并调用 kimi 无头模式（默认 auto 权限，工具自动批准）
PROMPT=$(sed -e "s/{{TODAY}}/$TODAY/g" -e "s/{{LAST_RUN}}/$LAST_RUN/g" agent/prompt.md)
kimi -p "$PROMPT"

# 3. 质量闸：JSON 可解析 + 声称有报告的条目文件确实存在
python3 - <<'EOF'
import json, pathlib, sys
d = json.load(open('data/products.json', encoding='utf-8'))
for p in d['products']:
    for k in ('domain', 'boards', 'report'):
        assert k in p, f"{p.get('domain')} 缺字段 {k}"
    if p['report']:
        assert pathlib.Path('docs', p['report']).exists(), f"{p['domain']} 的报告文件缺失"
print('校验通过，产品数:', len(d['products']),
      '，已有报告:', sum(1 for p in d['products'] if p['report']))
EOF

# 4. 重建产品总览页
python3 agent/build_index.py

# 5. 记录本次运行日期（即使无内容变化，检索窗口也要前移）
echo "$TODAY" > "$STATE"

# 6. git 提交并推送（GitHub Actions 构建 VitePress 并部署 Pages）
if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    git add -A
    git commit -m "chore: daily intel update $TODAY" >/dev/null
    git push
    echo "已推送，Actions 将自动部署"
    # 有新报告 / 新上榜域名 → tg-notify 通知（发送失败不中断流程）
    MSG=$(python3 agent/diff_notify.py "$SNAP")
    if [ -n "$MSG" ]; then
        echo "$MSG" | tg-notify || echo "警告：tg-notify 发送失败"
    fi
else
    echo "内容无变化，跳过提交"
fi
rm -rf "$SNAP"
echo "=== $(date '+%F %T') 完成 ==="
