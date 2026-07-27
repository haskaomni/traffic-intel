---
title: OpenFate
domain: openfate.ai
---

# OpenFate（openfate.ai）

> AI 驱动的八字命理与人生策略平台

## 产品是什么

OpenFate 是一个 AI 驱动的在线命理平台，由独立开发者运营（官网 FAQ 中自称「关于我」，未见团队或公司信息，待核实）。用户输入出生日期、时间、地点，即可免费生成八字（四柱）、紫微斗数、西方星盘命盘，再由 AI 把古典命理术语翻译成现代、可执行的人生建议，覆盖性格、事业、财富、感情等维度（[官网](https://openfate.ai/)）。除 C 端网站外，团队还开源了 `@openfate/bazi-mcp` MCP 服务，让 Claude、Cursor 等 AI Agent 可直接调用其确定性排盘引擎（[GitHub](https://github.com/openfate-ai/bazi-mcp)）。

## 核心功能

- **免费排盘工具**：八字四柱（含真太阳时校正）、紫微斗数十二宫、西方星盘查询，主打「零基础也能看懂」（[官网](https://openfate.ai/)）
- **AI 命理解读**：把日主强弱、五行喜忌、格局等概念翻译成平实语言的性格、事业财富、流年运势分析
- **AI 对话答疑**：用户可就命盘提问，官网显示已有 75,000+ 次 AI 智能对话
- **感情合盘**：八字 Compatibility 配对分析（[官网 insights](https://openfate.ai/en/insights/best-modern-bazi-ai-tool-openfate)）
- **开源 Bazi MCP 服务**：npm 包 `@openfate/bazi-mcp`，MIT 协议，已收录进 MCP Registry，供 AI Agent 做确定性历法计算（[GitHub](https://github.com/openfate-ai/bazi-mcp)）
- **多语言与内容体系**：支持中（简/繁）英，配有 Bazi 学习路径与运势专题内容站

## 流量表现

- trending 榜排名第 83 位，月访问量 112.1K，月增长 87.5K（环比增速约 +356%），首次被发现于 2026-01-27（traffic.cv 榜单数据）。
- 增长可能的原因（推测）：一是有用户反馈提到「意外在 Threads 上发现这个算命网站」，说明其通过社交媒体口碑传播；二是 2026 丙午火马年运程、犯太岁等应季内容契合年初华语圈命理搜索旺季（首次发现时间 1 月底与此吻合）；三是 SEO 内容站（insights 专题、llms.txt）在 AI 搜索场景下获取流量。

## 商业模式

免费增值 + 点数充值模式。排盘与基础解析免费；完整报告、深度问答、Manifestation Strategy 等「新的个性化内容」消耗点数（[定价页](https://openfate.ai/en/pricing)）。点数定价为 NT$245/250 点、NT$350/500 点、NT$600/1000 点（[繁中定价页](https://openfate.ai/zh-hant/pricing)），另有订阅档位（订阅者解释助手不限次）；失败的 AI 调用自动退还点数。

## 竞争格局

- **测测星座 / 准了**：国内头部命理 App，主打真人咨询师社区，OpenFate 则以 AI 自动生成报告为主，无真人服务。
- **Co–Star**：西方占星头部产品，美式年轻化文案风格，OpenFate 侧重八字/紫微等东方命理且面向华语用户。
- **The Pattern**：以性格与人际洞察为主的占星 App，OpenFate 的差异在于多体系（八字+紫微+星盘）+ 开放的 MCP 开发者生态。

## 情报判断

OpenFate 切中「东方命理 + AI 解读」这一在华语与海外华人圈需求稳定的赛道，用免费排盘工具做获客入口、点数充值变现，模型轻、边际成本低；同时开源 Bazi MCP 抢占 AI Agent 基础设施位，是少见的「C 端 + 开发者」双线打法。月增速超 350% 显示势能强劲，但基数尚小（11 万月访），且命理类产品的留存与付费意愿依赖「准不准」的主观口碑，可持续性有待观察。值得关注的点：MCP 服务能否成为其在 Agent 生态中的护城河。

---
*调研日期：2026-07-27 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
