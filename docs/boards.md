# 监控说明

## 数据源

本站监控 [traffic.cv](https://traffic.cv/) 的两张月度 traffic 榜：

| 榜单 | URL | 含义 |
| --- | --- | --- |
| new | `/leaderboard/traffic/{年}/{月}/new` | 本月新被检测到、且流量起量的域名 |
| trending | `/leaderboard/traffic/{年}/{月}/trending` | 本月增速最快的域名 |

traffic.cv 的数字是**多源建模的月度估计值**（非 analytics 导出），官方说法是
「排名方向正确、量级正确」——这正是竞品情报所需要的精度。
新榜单在每月 10 日左右发布上个月的数据；免费层每榜只显示 12 条未打码记录
（完整 100 条为 Pro 内容），本站即监控这 24 个可见席位。

## 每日流水线

1. **抓榜**：`agent/fetch_boards.py` 抓取两张榜，自动回退到最新非空月份，
   新出现的域名登记进 `data/products.json`。
2. **调研**：Kimi Code 无头智能体读取待调研队列（每次最多 8 个，trending 榜优先），
   逐个打开官网、检索公开报道，产出 `docs/products/<domain>.md` 中文报告。
3. **校验 + 重建**：JSON 结构与报告文件完整性校验通过后，
   `agent/build_index.py` 重建产品总览表。
4. **发布**：`git push` 触发 GitHub Actions 构建 VitePress 并部署到 GitHub Pages；
   有新报告时通过 Telegram 推送摘要。

## 目录约定

```
traffic-intel/
├── docs/                  # VitePress 源
│   ├── products/            # 每产品一份报告（智能体维护）
│   └── ...
├── data/
│   └── products.json        # 产品注册表（榜单数据 + 报告索引）
└── agent/
    ├── prompt.md            # 智能体任务书（调研方法 + 写入规范）
    ├── run.sh               # 每日入口（cron 触发）
    └── fetch_boards.py      # 榜单抓取
```

调整调研行为（每次调研数量、优先级、报告模板）：编辑 `agent/prompt.md`。
调整站点结构 / 主题：编辑 `docs/.vitepress/config.mts`。
