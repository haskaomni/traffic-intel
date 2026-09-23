---
title: GenOffice
domain: genoffice.ai
---

# GenOffice（genoffice.ai）

> Genspark 出品的开源 AI 办公套件

## 产品是什么

GenOffice 是 AI 创业公司 Genspark（创始人景鲲为前百度高管）于 2026 年 8 月 3 日发布的开源 AI 办公套件，号称「全球首个全功能开源 AI Office Suite」。它是一款 macOS / Windows / Linux 桌面客户端，本地打开和编辑 Word、Excel、PowerPoint、PDF、HTML、Markdown 六类文件，并把 AI 写作、数据分析、演示文稿生成直接内置进编辑器。官方称 Alpha 版由一名工程师用一周时间完成，消耗约 1 万美元 AI Token（[Genspark 官方博客](https://www.genspark.ai/blog/genoffice-open-source-ai-office)、[网易报道](https://www.163.com/dy/article/L3DJIJ1205566TJ2.html)）。

## 核心功能

- **GenOffice Docs**：打开/保存真实 .docx 文件，字节级保留原格式；可用一句 Prompt 起草、改写、重排版式（[官网](https://genoffice.ai/)）
- **GenOffice Sheets**：自研 .xlsx 引擎，支持图表、透视表、切片器；AI 可直接生成公式和预算表
- **GenOffice Slides**：原生 .pptx 编辑（母版、版式、参考线），描述主题即可生成整套演示文稿
- **PDF 工具**：直接编辑 PDF 文字和图片、批注和表单，本地免费将 PDF 转换为 Word/Excel/PPT
- **HTML / Markdown 编辑器**：生成单文件落地页、报告、海报；无干扰 Markdown 写作
- **AI 与 Agent 集成**：块级 AI 编辑带快照和 diff；所有命令同时是 MCP 工具，可被 Claude Code、Cursor 等 MCP 客户端直接调用（[GitHub README](https://github.com/genspark-ai/genoffice/blob/main/README.md)）

## 流量表现

- 榜单数据：new 榜 rank 35，月访问量 98K，月增长 98K，首次被发现于 2026-07-29。
- 月增长与月访问量同为 98K，说明该域名流量几乎全部是最近一个月新增——与产品 2026-08-03 发布即引发大量媒体报道的时间线吻合（MarkTechPost、新浪财经、网易等均有报道）。
- 增长可能的原因（推测）：一是「一人一周一万美元做出 Office」的故事性传播在中文科技圈引爆讨论；二是「免费、开源、无广告」对微软 Office / WPS 用户的吸引力；三是 Genspark 本身已有品牌声量（此前披露 12 个月做到 2.5 亿美元 ARR，见[网易报道](https://www.163.com/dy/article/L3DJIJ1205566TJ2.html)）。

## 商业模式

- 软件本身完全免费、无广告、无水印，Apache 2.0 开源（GitHub 仓库 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)）。
- AI 功能按 Genspark credits 计费，或自带 API Key（BYOK，支持 Claude、OpenAI、Gemini、DeepSeek 等）；免费额度与单价未公开（[ChooseAI 报道](https://www.chooseai.net/news/5487/)）。
- 开源仓库中 `ee/` 目录预留企业模块，适用单独的 GenOffice Enterprise License，企业版是潜在的变现方向（[ChooseAI 报道](https://www.chooseai.net/news/5487/)）。有实测用户反映重度使用 AI 功能账单近 60 美元，成本不低（[什么值得买](https://post.smzdm.com/p/ad7de09z)）。

## 竞争格局

- **Microsoft 365 Copilot**：办公套件的绝对巨头，AI 深度集成但订阅制、闭源；GenOffice 以免费开源 + BYOK 切价格敏感和隐私敏感用户。
- **WPS AI**：国内主流办公套件，同样走 AI 会员订阅路线；GenOffice 开源免费，对 WPS 用户迁移门槛低（已有用户在讨论「替换 WPS」，见[什么值得买](https://post.smzdm.com/p/ad7de09z)）。
- **LibreOffice / OnlyOffice**：老牌开源办公套件，但无原生 AI 能力；GenOffice 的差异化是「AI 一等公民」和 MCP/Agent 集成。
- **Notion / 飞书**：云端协作文档，主打协作而非本地文件兼容；GenOffice 走本地优先路线。

## 情报判断

GenOffice 能跑量主要靠三点：发布故事极强（一人一周一万美元）、免费开源直击 Office 订阅制痛点、以及 Genspark 已有的品牌和用户基础导流。短期流量爆发确定，但可持续性存疑：产品仍处 Alpha 阶段，复杂格式兼容性官方自己提示「需检查重要文件」，重度 AI 使用成本不低；开源后分叉门槛极低（已出现 HermesOffice 分叉项目）。值得关注的点是它的战略意图——不靠 Office 本身赚钱，而是抢占本地工作上下文入口，为 Genspark 的 Agent 和企业服务引流，这是一条值得持续跟踪的路线。

---
*调研日期：2026-09-24 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
