---
title: VoiceStudio
domain: voicestudio.sh
---

# VoiceStudio（voicestudio.sh）

> 本地运行的开源 AI 语音工作台

## 产品是什么

VoiceStudio 是由 debpalash 维护的开源桌面语音工作台，前身为 OmniVoice-Studio，定位为本地版 ElevenLabs 替代方案。它把语音克隆、音色设计、视频配音、听写、转写和有声书制作放进同一个应用，默认在用户设备上运行，支持 macOS、Windows、Linux 和 Docker（[GitHub](https://github.com/debpalash/VoiceStudio)）。

## 核心功能

- **Voice Cloning / Voice Design**：克隆经授权的声音或设计新音色，并在本地生成语音。
- **视频配音与长音频生产**：支持按时间轴配音、有声书、批量任务和可复用工作流。
- **听写与转写**：提供浮动听写组件和本地转写能力。
- **本地多引擎架构**：可从默认 VoiceStudio/OmniVoice 或其他引擎开始，官方语言目录标称覆盖 646 种语言；CPU 可用，GPU 用于加速。
- **Local API 与 MCP**：将本地语音能力开放给其他程序和 AI Agent。
- **隐私优先**：无需账户或云端，通常只在用户主动检查更新或下载模型时联网（[官网](https://voicestudio.sh/)）。

## 流量表现

- 榜单数据：new 榜第 23 名，月访问量 84.1K，月增长 79.9K，首次被发现于 2026-08-06，本月增长量接近当前总访问量。
- 增长可能原因（有公开迹象，渠道贡献仍属推测）：2026 年 9 月多家技术媒体报道其登上 GitHub Trending，并以「本地、开源的 ElevenLabs 替代」介绍项目；更名和开源社区传播可能共同推动访问增长（[Studeria，2026-09-10](https://www.studeria.fr/articles-de-blog/voicestudio-alternative-locale-elevenlabs-clonage-vocal)、[PromptCrates，2026-09-03](https://promptcrates.com/news/voicestudio-github-trending-local-elevenlabs)）。

## 商业模式

开源桌面版采用 AGPL-3.0，可免费使用；另有闭源 Pro 版本，官网标价 $99/年或 $299 买断，提供商业许可和额外功能，Cloud 版本仍显示为即将推出。项目也接受赞助和捐赠。需要注意，应用许可证与模型权重、音色等许可证相互独立，购买 Pro 并不自动取得所有模型的商业使用权（[官网](https://voicestudio.sh/)、[GitHub 许可说明](https://github.com/debpalash/VoiceStudio)）。

## 竞争格局

- **ElevenLabs**：云端语音生成与克隆体验成熟、部署省心；VoiceStudio 更强调本地隐私、可审计和可扩展。
- **RVC**：开源社区常用的实时/离线声音转换方案，更聚焦变声，不是完整语音生产工作台。
- **Piper**：轻量本地 Text to Speech，部署简单，但不覆盖 VoiceStudio 的配音、听写和有声书完整流程。

## 情报判断

VoiceStudio 同时抓住本地隐私、云端语音成本和 Agent 工具接入三个需求，GitHub 传播与榜单增长在时间上能够相互印证。其持续性取决于开源社区活跃度和安装体验；硬件差异、模型下载以及应用与模型许可证的复杂性，是普通用户和商业团队采用时的主要摩擦。

---
*调研日期：2026-10-17 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
