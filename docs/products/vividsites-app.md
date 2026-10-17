---
title: Vividsites
domain: vividsites.app
---

# Vividsites（vividsites.app）

> 一句话生成电影感 3D 网站的 AI 工作室

## 产品是什么

Vividsites 自称「the cinematic web studio」，是一个围绕「会动的网站」构建的产品：提供 315 个已上线的高质量 3D / shader / 滚动叙事（scroll-film）网站模板、112 个可一键安装的组件，以及一个名为 Create 的 AI 构建器——用户用一句话描述需求，Create 会从模板库匹配、生成 3D 模型与素材、自动构建并自检，最后交付完整代码、prompt 和在线 URL。团队/公司背景未公开（待核实），官网仅在页脚提到「1.1 万设计师在 Instagram 上关注」。

## 核心功能

- **Create AI 构建器**：输入一句话、参考 URL 或截图，约 5 分钟完成「选模板 → 生成 3D 资产 → 构建并截图自检 → 交付代码与 live URL」的全流程；构建基于 Claude Sonnet 5.5，Max 档可用 Claude Opus 5.5。
- **模板库（Templates）**：315 个已真实上线的网站模板（Landing / 整站），每个模板附带代码与生成它的 prompt，可浏览或用 Create remix。
- **组件库（Components）**：112 个 UI/3D 组件永久免费，含源码和一行命令安装（`npx shadcn@latest add https://vividsites.app/r/<name>.json`），兼容 Next、Vite 和纯 HTML。
- **Motion 片段**：52 段动效作品，每段附带 prompt、代码和 MP4。
- **MCP server**：Pro/Max 提供 MCP 服务，Claude、Cursor 等客户端可直接搜索模板库并拉取代码。

## 流量表现

- 榜单数据：月访问量 20K，月增长 +19.4K，首次被发现 2026-08-15，进入 traffic.cv **new 榜（rank 89）**，board_desc 无。
- 解读：新站上线约两个月即进入 new 榜，月增长接近总访问量（19.4K / 20K），说明流量几乎全部为近期新增，典型的「新发布冲量」形态。
- 增长可能原因（推测）：免费组件库 + shadcn 风格的一行安装命令天然利于在开发者社区传播；电影感 3D 站点在 Instagram 等视觉平台上易于展示（官网自称有 1.1 万 Instagram 关注者，待核实）。

## 商业模式

- **Free（$0 永久）**：浏览全部模板，组件库完整免费（代码 + 一键安装）。
- **Pro（$25/月）**：每天可复制 3 个模板 prompt、全部 motion 资源、Create 每月 8 次构建、商用授权、MCP server。
- **Max（$79/月）**：Create 每月 40 次构建，其中最多 13 次可跑 Claude Opus 5.5。
- **加量包**：$20 / 10 credits，永不过期，任何计划可用。
- 全计划 7 天退款保证；Create 无免费构建额度（构建失败自动退款）。

## 竞争格局

- **21st.dev / v0（Vercel）**：同样是组件/页面生成 + 复制代码模式；Vividsites 差异在专攻 3D / shader / 滚动电影感站点，而非通用 UI。
- **Framer / Webflow AI**：整站 AI 构建但偏托管建站闭环；Vividsites 交付的是完整代码，面向开发者。
- **Wegic / Durable 等 AI 建站**：面向小白的「一句话建站」；Vividsites 面向设计师和前端开发者，产出可直接进生产工程。

## 情报判断

Vividsites 切中了「Awwwards 级 3D 网站制作成本高」的痛点，用「已上线模板 + 全代码交付 + shadcn 式安装」降低门槛，且后端构建直接跑在 Claude 模型上、以 credit 计价，成本结构清晰、商业化动作完整（Free/Pro/Max 三档 + 加量包）。风险在于月增 19.4K 是否靠发布期流量脉冲，3D 站点是否只是一阵风尚需观察；可持续关注的点是免费组件库能否持续带来自然流量，以及 MCP 接入能否绑定 Claude/Cursor 生态的开发者用户。团队背景与融资情况公开信息极少，待核实。

---
*调研日期：2026-10-18 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + [官网](https://www.vividsites.app/)（[Pricing](https://www.vividsites.app/pricing)、[Templates](https://www.vividsites.app/templates)） + 公开报道*
