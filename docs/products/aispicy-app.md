---
title: AI Spicy
domain: aispicy.app
---

# AI Spicy（aispicy.app）

> 上传照片生成成人向 AI 形象的图片工具

## 产品是什么

AI Spicy 是一个 AI 图片生成网站，核心玩法是「上传一张照片，让 AI 生成你从未见过的另一面」，从其官方 Facebook 广告投放文案（"Upload a photo and let AI reveal a side you've never seen before. Unlock The Unexpected."）可以确认这一定位（[Facebook 广告](https://www.facebook.com/61591586293620/posts/upload-a-photo-and-let-ai-reveal-a-side-youve-never-seen-before/122113945575386209/)）。官网为 Nuxt 客户端渲染站点，页面配置中泄露的内部项目路径为 `aicosplay-html/adult-applet`，表明它出自一套「AI cosplay 成人向小程序」代码体系。运营方/公司背景未在官网公开，待核实。

## 核心功能

官网为纯前端渲染，公开文案极少，以下功能点来自官网前端资源与广告落地页的可观察证据：

- 照片转 AI 形象（photo-to-image）：广告落地页路径为 `/acp-to-image`，即上传照片生成 AI 图片（[urlquery 抓取记录](https://urlquery.net/report/7cdc225a-9d3e-4211-a2fe-09d74f53dfd2)）
- 成人向（NSFW）内容方向：内部代码路径含 `adult-applet`，广告投放也走「spicy」暗示路线
- 订阅 + 积分包双变现组件：官网前端预加载 `SubscriptionModal` 与 `CreditPacks` 模块
- 多语言全球化：站点内置 24 种语言（英、日、韩、法、德、西、葡、阿、希等），按浏览器语言自动跳转
- 移动端子站 `m.aispicy.app` 与 PC 站并行，移动端优先
- 技术栈使用 Firebase（鉴权/分析）与 PostHog（行为分析）

## 流量表现

- 月访问量 144.5K，月增长 +133.2K（即上月基数仅约 1.1 万，单月环比约 12 倍），2026-06-26 首次被收录，登上 traffic.cv trending 榜第 69 名。
- 增长原因（有依据的推测）：urlquery 记录显示其落地页 URL 携带 `fbclid`（Facebook 广告点击标识）与 `ad=` 参数，且存在多个 Facebook 广告账号在投放同一套素材，说明这波增长主要由 Facebook 付费投放驱动，而非自然流量。
- 值得注意的是安全口碑偏弱：ScamAdviser 给出 51 分信任分（[ScamAdviser](https://www.scamadviser.com/check-website/aispicy.app)），Gridinsoft 给出 42/100 并提示「新域名警告」（[Gridinsoft，2026-07-25](https://gridinsoft.com/online-virus-scanner/url/aispicy-app)）。

## 商业模式

定价页未公开（官网无独立 pricing 页面，需在站内触发弹窗）。从前端模块可确认采用「订阅（Subscription）+ 积分包（Credit Packs）」混合变现，这是成人向 AI 图片站的主流模式；具体价格档位待核实。

## 竞争格局

- Candy.ai：AI 女友陪伴 + 图片生成，重聊天陪伴场景，AI Spicy 更偏「照片变身」工具属性
- SoulGen：AI 图片生成（含 NSFW），以文本/参考图生成为主，订阅制
- Promptchan：纯 NSFW AI 图片生成社区，带作品广场
- CrushOn.AI：NSFW 角色聊天为主，图片为辅

AI Spicy 的差异点在于「上传真人照片一键生成」的低门槛玩法和强广告投放打法。

## 情报判断

这是一个典型的「广告买量型」成人向 AI 图片站：12 倍的单月增长几乎可以直接归因于 Facebook 投放（落地页带 fbclid 是直接证据），产品本身没有公开团队、没有媒体报道，技术上是标准化的 Firebase + Nuxt 模板工程。可持续性存疑——增长完全依赖广告 ROI，且低信任分、成人内容方向使其面临支付通道与广告平台政策的双重风险；但短期套利模型（低门槛上传玩法 × 订阅 + 积分）在 NSFW 赛道被反复验证有效，值得作为「投放驱动型 AI 站」样本持续跟踪。

---
*调研日期：2026-09-19 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
