---
title: Uselink
domain: uselink.app
---

# Uselink（uselink.app）

> 把 HTML / Markdown 变成可评论的分享链接

## 产品是什么

Uselink 是一个文档托管与分享工具：粘贴 HTML、Markdown 或 AI 生成的草稿，即可获得一个归自己 handle 所有的公开链接，无需部署、读者无需注册。它解决的核心痛点是「AI 生成的漂亮页面/报告困在聊天窗口里无法干净分享」——创始人 Nathan Tran 在 Product Hunt 上自述自己不是工程师，经常用 Claude 生成 one-pager、报告和 landing page，却只能截图或发源码。产品目前处于 alpha 阶段，据其自述整个应用两周内开发完成（来源：[Product Hunt 讨论页](https://www.producthunt.com/products/uselink)）。

## 核心功能

- 粘贴 HTML / Markdown 即时生成可控 URL，交互式 HTML 可真实运行（图表、仪表盘可正常渲染）
- 免注册线程评论：读者无需账号即可在页面上按段落锚定评论，评论跨版本保持锚定
- 链接访问控制：密码、有效期、浏览次数限制，可指定发布对象，workspace 邀请制
- 版本历史：每次保存生成不可变版本，可 diff、可回滚，链接始终指向最新版
- 可视化编辑器：无需写代码即可编辑已上线页面（官方称类似 Figma 的布局系统）
- MCP 服务器：Claude、Cursor、n8n 可直接代为发布页面

（来源：官网 uselink.app 首页描述 + [Product Hunt 产品页](https://www.producthunt.com/products/uselink)）

## 流量表现

- 榜单数据：traffic.cv new 榜 rank 101；月访问量 18.8K，月增长 18.8K（即本月几乎全部流量为新增）；首次被发现 2026-05-21。
- 增长几乎全部来自上线爆发：Uselink 于 2026-06-03 在 Product Hunt 发布，当日获 Day Rank 第 9 名、137 票（来源：[PH 每日热榜](https://decohack.com/producthunt-daily-2026-06-04/)）。**推测**：18.8K 的新增访问主要由这次 PH 上线及配套营销活动（据创始人自述营销物料 5 天内完成）驱动。
- 注意 first_seen（2026-05-21）早于 PH 上线日（2026-06-03），说明网站在正式发布前约两周已可访问，或此前有一次小规模预热（待核实）。

## 商业模式

官网定价页已上线（来源：uselink.app/pricing 页面描述）：

- 免费档：3 篇文档
- Solo：$4/月起（按年付），含 500 篇文档、自定义域名、密码链接、数据分析
- Teams：$19/月按 workspace 固定收费，不按席位计费

创始人在 PH 评论区表示定价「会保持平价、无意外账单、无厂商锁定」，并考虑为轻度用户设「一杯咖啡」低价档。

## 竞争格局

- **Google Docs / Notion**：通用文档协作，但交互式 HTML 无法正常渲染，且评论需要账号——Uselink 的免注册评论是主要差异点（来源：[PH 介绍](https://www.producthunt.com/products/uselink)）。
- **pageplane.app**：同为「托管 AI 聊天生成的 HTML」的个人项目，功能更简陋；其作者在 PH 评论区公开承认 Uselink 实现更好。
- **tiiny.host**：老牌静态 HTML 托管分享服务，偏托管本身，缺少评论、版本历史与 AI 工具链（MCP）集成。

## 情报判断

Uselink 精准踩中了「AI 生成内容的最后一公里」：大量非工程用户用 Claude 等生成 HTML 页面后无法优雅分享，这个痛点随 vibe coding 普及在扩大，MCP 服务器的接入又让它顺势成为 AI 工作流的发布出口。短期流量靠 Product Hunt 上线脉冲，可持续性取决于能否把一次性分享用户转化为留存用户——免费额度只有 3 篇文档，转化设计比较激进。值得关注的点：一是 MCP 集成能否在 Claude/Cursor 用户中形成口碑传播；二是赛道门槛低（竞品作者两周可复刻核心功能），护城河主要在评论/版本历史的体验深度。

---
*调研日期：2026-07-27 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
