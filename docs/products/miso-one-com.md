---
title: Miso One
domain: miso-one.com
---

# Miso One（miso-one.com）

> Miso TTS 8B 开源语音模型的演示与托管站点

## 产品是什么

Miso One 是围绕 Miso Labs 发布的 Miso TTS 8B 模型建立的产品化站点——一个 80 亿参数、开放权重的英文 TTS 模型，主打富有情感表现力的对话式语音。模型由 Miso Labs 于 2026 年 6 月 3 日以修改版 MIT 协议开源发布（[MarkTechPost 报道](https://www.marktechpost.com/2026/06/04/miso-labs-releases-misotts-an-8b-emotive-text-to-speech-model-with-open-weights/)）。miso-one.com 的 [About 页](https://miso-one.com/about)自述为 Miso TTS 8B 的「信息与演示站点」，同时提供托管版语音生成、Voice Design 和 Voice Clone 等付费服务。开发者可下载开源权重本地部署，普通用户可直接用站点 demo 生成语音。

## 核心功能

- **开源权重 TTS**：Miso TTS 8B 开放权重，修改版 MIT 协议，权重托管于 Hugging Face，支持本地 CUDA 推理（来源：[MarkTechPost](https://www.marktechpost.com/2026/06/04/miso-labs-releases-misotts-an-8b-emotive-text-to-speech-model-with-open-weights/)）
- **对话式情感语音**：采用 Sesame CSM 风格架构（7.7B backbone + 300M 音频解码器），可根据音频上下文对说话人语气做出回应
- **One-shot 声音克隆**：约 10 秒音频提示即可做 voice continuation / 声音克隆
- **低延迟生成**：官方宣称 110ms 生成延迟，对比 ElevenLabs 700ms、Sesame 300ms（厂商宣称，未经第三方验证）
- **Voice Design / 私有声音模型**：付费订阅中提供声音设计预览与私有声音模型创建（按 credits 计费）
- **默认音频水印**：生成音频默认带 SilentCipher 水印

## 流量表现

- 榜单数据：new 榜 rank 84，月访问量 22.7K，月增长 22.7K（即上月几乎从零起步的纯增量），首次被发现 2026-06-04。
- 流量曲线与模型发布时间高度吻合：Miso TTS 8B 于 2026 年 6 月 3 日开源，站点 6 月 4 日即被榜单捕获，当月全部 22.7K 访问均为新增。
- 增长原因（推测）：开源权重发布带来大量模型意图搜索（找权重、demo、部署文档），该站点卡位「Miso One / Miso TTS」关键词的 SEO 内容页承接了这波搜索流量；其页面大量结构化 FAQ、「What is Miso One」式内容即为此设计。

## 商业模式

托管订阅制 + credits：免费用户每次转换限 120 字符；付费档位为 Basic $9.9/月（年付 $4.95/月，96 万字符/年）、Pro $29.9/月（年付 $14.95/月，420 万字符/年）、Enterprise $49.9/月（年付 $24.95/月，960 万字符/年），credits 在 TTS、Voice Design、Voice Clone 之间共用，付费档单次转换上限 1,000 字符。底层模型本身开源免费，变现的是托管与声音克隆等增值服务。

## 竞争格局

- **ElevenLabs**：闭源托管 TTS 龙头，多语言、生态成熟；Miso One 以开源权重与英文对话式低延迟为差异点。
- **Sesame (CSM)**：Miso TTS 架构的直接参照系，同属对话语音模型；Miso 以开放权重对比 Sesame 的有限开放。
- **Fish Audio / Qwen3 TTS 等开源 TTS**：同类开源语音模型，Miso TTS 8B 的差异化在 RVQ 词表扩展与语气条件化生成。
- 另需说明：miso-one.com 自身更像围绕模型流量的 SEO + 托管变现站点，与「克隆 Miso One」式蹭流站点（如 qwen3tts.com 的相关博客）同处一个生态位。

## 情报判断

这是典型的「开源模型发布 → SEO 站点承接搜索流量 → 托管订阅变现」打法：模型开源当天上线信息站，抢占模型名搜索入口，月增长几乎全靠发布初期的搜索红利。可持续性存疑——流量随模型热度衰减，且 miso-one.com 是否为 Miso Labs 官方站点存疑（About 页自称「信息与演示站点」，未明确声明官方身份，待核实）。值得关注的点是托管订阅定价明显低于 ElevenLabs 同类产品，若 Miso TTS 8B 口碑成立，这类低价托管站有真实的转化空间。

---
*调研日期：2026-07-27 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
