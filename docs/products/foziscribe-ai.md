---
title: FoziScribe
domain: foziscribe.ai
---

# FoziScribe（foziscribe.ai）

> 基于 Whisper 的 AI 音频转写工具

## 产品是什么

FoziScribe 是一款 AI 音频转写 SaaS，由印度德里的 Zapiwala AI 运营（来源：[官网 Cookie Policy](https://foziscribe.ai/cookies)）。它基于 OpenAI Whisper 模型，支持 99 种语言的自动识别转写，输出带精确时间戳的文本。产品面向内容创作者、记者、研究人员和团队，使用方式为网页端拖拽上传音频（MP3/WAV/M4A/OGG/FLAC/WebM，最大 50MB），数秒内返回转写结果，可复制或下载为 .txt。除转写外，官网还强调「检测语音自然停顿时间戳」的差异化卖点——帮助短视频创作者按语音节奏切分场景，并提供 Text to Audio（语音合成）和 Script to Magical Prompt Generation（脚本生成图像提示词）功能（来源：[官网](https://foziscribe.ai/)）。

## 核心功能

- **99 语言转写**：自动检测语言，无需手动选择，基于 OpenAI Whisper，宣称清晰音频准确率超 95%
- **智能时间戳**：逐词、逐段精确时间戳，可定位到录音任意时刻
- **自然停顿检测**：找出配音中的自然停顿点，用于视频场景切分（主打差异化功能）
- **Text to Audio**：付费档附赠每月语音合成时长
- **Script to Prompt Generation**：将脚本转为图像生成提示词
- **隐私设计**：宣称音频不落地存储，内存处理后即丢弃

## 流量表现

- new 榜排名 28，月访问量 75.8K，月增长 75.8K（即本月访问全部为新增），首次被发现 2026-06-06。
- 从首次发现到上榜约 7 周，75.8K 的月访问对一个新站属于中等偏上水平，说明上线初期获得了较集中的流量导入。
- 增长可能原因（推测）：运营方 Zapiwala AI 在 YouTube 上发布 AI 工作流类内容（如 [Glimpse 收录的其频道视频](https://glimpse.wozart.com/v/ixjqngvz)），可能通过自有内容渠道为产品导流；此外「停顿时间戳切场景」的短视频创作工作流定位，契合当前 AI 视频生成的热点需求。具体获客渠道待核实。

## 商业模式

Freemium 订阅制，以印度卢比计价（来源：[官网定价页](https://foziscribe.ai/)）：

- **Free**：₹0/月，每月 10 分钟转写（Fast 模式）
- **Creator Pro**：₹499/月，400 分钟转写 + 65 分钟 Text to Audio
- **Growth**：₹1,499/月，2000 分钟转写 + 330 分钟 Text to Audio
- **Unlimited**：₹4,999/月，转写与语音合成均不限量

计费以音频分钟数为额度单位（Fast 模式 1 分钟 = 1 credit，Best 模式 1 分钟 = 2 credits）。

## 竞争格局

- **TurboScribe**：同属 Whisper 系转写工具，不限量低价策略，但无停顿检测与视频工作流功能
- **Otter.ai**：英文会议场景为主，强项在实时转写与协作，语言覆盖远少于 99 种
- **Riverside / Descript**：面向播客与视频剪辑的一体化工具，转写只是其中一环，价格更高
- **Whisper 官方 API 套壳工具群**：同质化严重，FoziScribe 靠「停顿时间戳 → 场景切分」的创作者工作流叙事做区隔

## 情报判断

FoziScribe 本质上是 Whisper API 的包装产品，技术壁垒低，但其选了一个聪明的叙事角度：把转写时间戳重新包装成「AI 短视频场景切分工作流」的关键一环，直接对接 AI 视频生成的流量红利。印度本土定价 + 自有 YouTube 内容渠道的组合，使其早期获客成本可能极低。可持续性存疑：Whisper 套壳工具竞争白热化，核心功能易被复制，需观察其能否在创作者工作流上建立真实留存。值得关注的点：它能否从转写工具进化为完整的「脚本→配音→分镜」创作管线。

---
*调研日期：2026-07-27 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
