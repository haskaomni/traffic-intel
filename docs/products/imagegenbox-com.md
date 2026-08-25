---
title: ImageGenBox
domain: imagegenbox.com
---

# ImageGenBox（imagegenbox.com）

> 多模型聚合的在线 AI 图像生成工具

## 产品是什么

ImageGenBox 是一个在线 AI 图像生成网站，聚合 Flux AI / Flux Pro、GPT Image 1.5 / GPT Image 2、Nano Banana、Seedream / Seedream 4.0 等多个第三方图像模型，提供 text-to-image 与 image-to-image 生成，并附带 styles 风格模板、templates、community 作品广场等功能（来源：[官网](https://imagegenbox.com) 路由结构及前端资源）。站点为 Nuxt/Vue 单页应用，使用 Firebase 登录（Google / 邮箱），支持 12 种语言，其中包含印尼语、马来语、菲律宾语、泰语等东南亚语种。运营团队/公司未公开：其 API 返回的 contact_us 中 company、address 字段均为空，域名 WHOIS 也已隐藏注册人（Amazon Registrar，[WHOIS 记录](https://whois.registrar.amazon)），团队背景待核实。

## 核心功能

- text-to-image：文生图，可在多个模型间切换（Flux、GPT Image、Nano Banana、Seedream 等）
- image-to-image：图生图 / 参考图生成
- styles：大量预设风格模板（3D 人偶、儿童绘本、美式 LinkedIn 职业照、赛博朋克、针织风等，后端配置有 200+ 功能项）
- 图像编辑类：IMAGE_REPAIR（修复）、IMAGE_ENHANCER（增强/放大）、REMOVE_BACKGROUND（抠图）、FACE_SWAPPER（换脸）、HEADSHOT（证件/职业照）
- 图生视频特效：kiss、dance 等热门玩法（每次 80 credits，后端配置）
- my-works / community：个人作品管理与作品广场

## 流量表现

- 榜单数据：new 新品榜 #61，月访问量 37.7K，月增长 37.7K（即上线首月几乎全部为新增量），首次被发现 2026-06-25（[traffic.cv 榜单](https://traffic.cv/)）。
- 域名注册时间为 2026-06-25（[WHOIS](https://whois.registrar.amazon)），与 first_seen 同日，属上线即被监控捕获的全新站点。
- 增长原因（推测）：站点 robots.txt 为 `Disallow: /` 全站屏蔽搜索引擎抓取，几乎排除 SEO 渠道；结合 12 语种（含 4 个东南亚语种）的本地化配置与低价试用（$0.10）转化设计，流量更可能来自付费投放 / 社媒导流，此点为推测，无直接证据。

## 商业模式

订阅制 + credits 点数（来自其公开定价接口 `api.imagegenbox.com/v1/price/data`，截至调研日仅见一个默认套餐）：

- PRO Trial Plan：$0.10 试用 1 天（含 500 trial credits），到期续费 $49.90/月，每月 5000 credits
- 付费可访问全部 PRO 工具、无水印下载；支持 PayPal、银行卡、Apple Pay、Google Pay
- credits 按功能计价：文生图/风格模板约 20 credits/次，图生视频特效 80 credits/次

## 竞争格局

- Pollo AI / Monica 等多模型聚合站：同样聚合 Flux、Nano Banana、Seedream 等模型，ImageGenBox 差异在东南亚多语言与低价试用钩子
- Magic Hour / ImagineArt：免费额度更厚、有公开社区与 SEO 内容，ImageGenBox 则无公开内容运营
- PhotoAI / HeadshotPro 类单品工具：只做职业照细分，ImageGenBox 是"大而全"模板超市打法

## 情报判断

典型的"模板站"打法：注册即上线、多语言铺量、$0.10 低价试用转 $49.9/月订阅，首月 37.7K 访问量说明投放/导流已有初步成效。风险点同样明显：robots 全站屏蔽意味着放弃自然搜索，增长完全依赖付费流量，可持续性存疑；团队匿名、支付走第三方白标收银（页面资源指向 thispay.net / soouya.com，待核实归属），需留意此类站点"快速起量—快速换壳"的常见路径，建议持续跟踪其访问量能否在次月维持。

---
*调研日期：2026-08-26 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
