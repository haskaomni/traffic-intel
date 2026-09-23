---
title: Is Agentic
domain: is-agentic.com
---

# Is Agentic（is-agentic.com）

> 网站 AI Agent 友好度打分工具

## 产品是什么

Is Agentic 是 Vercel 于 2026 年 8 月推出的免费在线检测工具，由 Ora（era labs 旗下的 agent-experience 研究公司）提供评分引擎（[MarkTechPost](https://www.marktechpost.com/2026/08/23/vercel-introduces-is-agentic-a-free-agent-readiness-scoring-tool-that-audits-public-websites-using-oras-100-checks/)、[Ora 官方博客](https://ora.ai/blog/is-agentic-with-vercel)）。它解决的问题是：当 AI Agent 成为网站的重要访问者，如何量化一个网站对 Agent 的「可发现、可访问、可理解、可使用」程度。用户输入任意公开 URL 即可获得一份分数报告和可执行的优化建议。

## 核心功能

- **Agent 就绪度评分**：基于 Ora 的 118 项检查，覆盖 discovery、access、usability、payments 四个层面，Vercel 将其重组为 Essential（80 分）、Recommended（20 分）、Bonus（5 分）三档权重（[MarkTechPost](https://www.marktechpost.com/2026/08/23/vercel-introduces-is-agentic-a-free-agent-readiness-scoring-tool-that-audits-public-websites-using-oras-100-checks/)）
- **不适用检查自动豁免**：网站没有 API、MCP、支付等接口时不会被扣分
- **逐条证据与建议**：每项发现附带扫描中观察到的证据和可直接落地的修复建议，改完可重新扫描对比
- **Observed agent journey**：报告中记录一个真实 Agent 浏览该站的路径及卡点，作为辅助证据
- **多格式机器可读报告**：同一 URL 支持 HTML、Markdown 输出，并提供公共 JSON API 和 MCP Server，可直接集成进 Agent 工作流，全部只读、无需密钥（官网文档）

## 流量表现

- 榜单数据：new 榜 rank 72，月访问量 45.3K，月增长 45.3K（即从 0 起步的纯新增），首次发现 2026-08-19
- 增长原因（有依据的推测）：产品 2026 年 8 月下旬上线，由 Vercel 官方渠道背书推广（[Vercel 官方 X 账号](https://x.com/vercel/all)），上线一周内即有 MarkTechPost 报道及中文圈 Threads、CSDN、博客园的传播（[Threads](https://www.threads.com/@maylogger_designer/post/DcZwlEfkqxz/)、[Kuro Hsu 博客](https://kurohsu.dev/notes/is-agentic-agent-readiness-audit.html)）。「输入网址立刻出分」的轻量形态天然适合社交分享，首月 45.3K 访问属发布期流量，后续能否维持待观察。

## 商业模式

完全免费，无付费计划、订阅或按次收费（[MarkTechPost](https://www.marktechpost.com/2026/08/23/vercel-introduces-is-agentic-a-free-agent-readiness-scoring-tool-that-audits-public-websites-using-oras-100-checks/)）。官网无定价页（/pricing 返回 404）。对 Vercel 而言，这更像是推动「agentic web」生态和引导站点改造（最终利好其托管业务）的获客型工具；Ora 则借此获得其评分引擎的曝光。

## 竞争格局

- **Cloudflare isitagentready.com**：同样免费秒级打分，但按 Cloudflare 自己的方法论评分（[agent-ready.dev 对比文](https://agent-ready.dev/agent-ready-vs-alternatives)）
- **Agent Ready（agent-ready.dev）**：第三方审计工具，宣称按公开规范而非厂商自定方法论评分
- **agentsfirst.dev**：提供 Agent Readiness 评级报告（Level 1-4），偏人工/半自动评测
- 差异：Is Agentic 的差异化在于 Vercel 品牌背书 + Ora 引擎的 100+ 检查项 + MCP/JSON 机器接口，天然面向 Agent 工作流集成。

## 情报判断

这是大厂（Vercel）定义新赛道的动作——把「Agent 友好度」做成类似 Lighthouse 之于性能的行业标准指标。免费 + 一键出分 + 报告可分享的形态极易传播，首月 45.3K 访问主要靠发布势能。可持续性取决于它能否成为事实标准：工具本身无锁定、无收入，长期价值在于引导站长按 Vercel/Ora 的规范改造网站。值得关注的点：评分方法论之争（Cloudflare 已跟进同类产品）、以及该分数是否会被 Agent 平台用作站点筛选信号。

---
*调研日期：2026-09-24 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
