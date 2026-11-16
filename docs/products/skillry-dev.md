---
title: Skillry
domain: skillry.dev
---

# Skillry（skillry.dev）

> 精选 Agent Skills 工作流库

## 产品是什么

Skillry 是面向 Claude Code、Codex、Cursor 等 AI Agent 的精选 Skills 库，把幻灯片、网页、图片和视频制作方法封装成可重复安装的 `SKILL.md` 工作流。公开报道显示其由中国独立开发者 Yihui 于 2026 年 8 月推出；官网称 400 多个 Skills 均由内部团队设计、编写、测试并持续更新，而不是简单抓取外部目录（[官网](https://skillry.dev/)、[上线与团队报道](https://www.xmsumi.com/detail/4298)）。

## 核心功能

- 覆盖 Slides、Web、Images、Video 等任务，每个 Skill 包含指令、模板和脚本。
- 每个条目展示实际生成结果，视频案例可对照原作品、复刻版本与提示词。
- 支持通过 MCP、CLI、安装提示词或 ZIP 将工作流交给 Agent。
- 浏览器授权后即可安装，Skillry 自身不要求 API Key；部分生成任务仍需用户自己的模型服务 Key。
- MCP 与 CLI 支持检查、更新已安装 Skills，更新前保留旧版本备份（[官网](https://skillry.dev/)）。

## 流量表现

- 榜单数据：trending 榜第 33 名，月访问量 535.8K，月增长 507K，首次被发现于 2026-08-26，本月访问量绝大部分来自新增量。
- 增长可能原因（有公开迹象，渠道贡献仍属推测）：其关联的 `awesome-opus5-5-videos` 项目把热门视频、复刻结果和完整提示词放在一起，9 月底至 10 月获得大量社交媒体转发；官网也集中展示了这些传播记录，内容资产与 Agent Skills 目录形成了互相导流的结构（[GitHub 项目讨论](https://gitnova.dev/en/r/yihui-dev/awesome-opus5-5-videos)、[官网](https://skillry.dev/)）。

## 商业模式

订阅与买断并行，均可访问全部 Premium Skills，每日可加载 50 次。标准价为月付 $19.9、年付 $158、Founding Lifetime 一次性 $249；截至调研日，官网黑五促销价分别为首月 $9.99、首年 $79 和买断 $169，订阅续费恢复标准价，促销活动标注于 2026-11-30 截止（[官网定价](https://skillry.dev/)）。

## 竞争格局

- **Cola Skill**：精选 Agent Skills 目录；Skillry 更强调自制模板、实际结果和后续维护。
- **Tenten Skills Atlas**：覆盖多类技能与教程；Skillry 在代码驱动视频、动效案例和提示词对照上更集中。
- **GitHub 开源 Skills 仓库**：免费且选择广，但质量与维护不一；Skillry 以筛选、测试和统一标准收取订阅费。

## 情报判断

Skillry 的核心不是“又有一个 Skills 目录”，而是把审美参考、可复现提示词和安装工作流连成一体，热点视频库又为付费目录提供了自然传播素材。可持续性取决于自制内容能否持续领先免费仓库，以及 Agent 生态变化后维护成本是否可控；每日加载额度也说明其在控制高频抓取与滥用。

---
*调研日期：2026-11-17 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
