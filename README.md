# Traffic 新品情报 · traffic-intel

监控 [traffic.cv](https://traffic.cv/) 流量榜单（new / trending）的情报站：
**智能体每日自动调研新跑出来的产品**，逐个打开官网、检索公开信息，
为每个产品生成一份中文 Markdown 报告，用 VitePress 发布到 GitHub Pages。

线上地址：<https://haskaomni.github.io/traffic-intel/>

## 架构（数据与展示分离）

```
traffic-intel/
├── docs/                    # VitePress 源
│   ├── .vitepress/config.mts  # 站点配置（侧边栏从 data/products.json 生成）
│   ├── index.md               # 首页
│   ├── boards.md              # 监控说明
│   └── products/              # 每产品一份报告（智能体维护）
├── data/
│   └── products.json          # 产品注册表：榜单数据 + 报告索引
└── agent/
    ├── prompt.md              # 智能体任务书（调研方法 + 写入规范）
    ├── run.sh                 # 每日入口：抓榜 → kimi 无头 → 校验 → push
    ├── fetch_boards.py        # traffic.cv 榜单抓取（自动回退最新非空月份）
    ├── build_index.py         # products.json → docs/products/index.md 总览
    ├── diff_notify.py         # 新增报告 → Telegram 通知文案
    ├── last_run               # 上次运行日期
    └── update.log             # cron 日志
```

## 每日自动更新流程（crontab 每天 06:23 触发）

1. `fetch_boards.py` 抓取当月 traffic 榜 new / trending 两页（免费层每榜可见
   12 条），新域名追加到 `data/products.json`（`report=null` 进入待调研队列）。
2. `run.sh` 把当天 / 上次日期注入 `agent/prompt.md`，以 `kimi -p` 无头模式执行：
   智能体对待调研产品逐个 FetchURL 官网 + WebSearch 检索，
   写 `docs/products/<domain>.md` 报告并回填注册表（每次最多 8 个）。
3. 质量闸：JSON 结构校验 + 报告文件存在性检查，失败则中断不推送。
4. `build_index.py` 重建产品总览页；有变化则 `git push`，
   GitHub Actions 自动构建 VitePress 并部署 Pages；
   有新报告时经 `tg-notify` 发 Telegram 通知。

## 手动操作

```bash
python3 agent/fetch_boards.py   # 只抓榜单
python3 agent/build_index.py    # 重建产品总览页
agent/run.sh                    # 手动跑一次完整更新
npm install && npm run dev      # 本地预览站点
```

调整智能体行为（调研数量、优先级、报告模板）：编辑 `agent/prompt.md`。
调整站点结构 / 主题：编辑 `docs/.vitepress/config.mts`。

## License

MIT
