---
title: YoFont
domain: yofont.com
---

# YoFont（yofont.com）

> 一句话生成多语言 AI 字体

## 产品是什么

YoFont 是一个 AI 字体生成器：输入一句风格描述或上传参考图（logo、海报、手写稿），即可生成一整套可安装的真实字体（不是 Unicode 仿字符图片），并配有在线 Studio 可逐字形修复或重绘。支持 TTF / OTF / WOFF / WOFF2 导出与 CDN @font-face 嵌入，官方宣称一次生成可覆盖 60 种语言、10 种书写系统（Latin、Cyrillic、Greek、Hebrew、Devanagari、中日韩等）。首个字体免费、无需绑卡。团队/公司背景未见公开披露（待核实）。

## 核心功能

- 一句话或参考图生成完整字体家族，最多 3 个字重（Thin / Regular / Bold）
- 单次生成覆盖 60 种语言、10 种书写系统，官方自称「唯一的多书写系统 AI 字体生成器」
- Studio 逐字形编辑：单个字符可重新生成、重绘或上传参考
- 导出 TTF / OTF / WOFF / WOFF2，或直接从 CDN 用 @font-face 嵌入网页
- Figma 插件（已上线，可从截图复制排版风格）；Chrome 扩展（待上线）
- 公共字体库（已收录 1 万+ 字体）、API 与 MCP server（Pro 及以上开放，供 Claude Code、Cursor 等调用）

## 流量表现

- 月访问量 303.9K，月增长 255.3K（增长量约为存量的 5 倍，处于爆发期），位列 trending 榜第 47 名；2025-06-25 首次被榜单发现。
- 增长可能原因（推测）：其一，「AI 生成真实可安装字体」是差异化明显的品类，市面上多数「font generator」只输出 Unicode 仿字符，YoFont 定位清晰利于传播与 SEO；其二，官网铺设了大量长尾 SEO 页面（cyrillic-font-generator、compare 对比页等），2026 年 7-8 月集中更新，符合近月流量陡增的节奏；其三，「首个字体免费 + 无需信用卡」降低尝试门槛。

## 商业模式

订阅制，按「字形（glyph）」计量（[定价页](https://yofont.com/plans)）：

- Free：$0，含 100 字形，仅预览与编辑，不可下载，字体公开
- Starter：$9/月，500 字形/月，可下载
- Pro：$19/月，5,000 字形/月，开放 API/MCP、商用授权、私有字体
- Studio：$49/月，15,000 字形/月，解锁最高细节模型（Nietzsche）
- 超量按字形加购（$0.008–0.015/字形）；商用授权随 Pro 以上套餐提供

## 竞争格局

- Creative Fabrica Font Generator：AI 生成真实 TTF，但仅 TTF 单格式、绑定 CF 生态的 coin 体系（[YoFont 官方对比页](https://yofont.com/compare/yofont-vs-creative-fabrica)）
- Lipi.ai：AI 字体生成 + 市集模式，但仅覆盖 Latin，无多书写系统与字重（[YoFont 官方对比页](https://yofont.com/compare/yofont-vs-lipi)）
- LingoJam 等复制粘贴式「font generator」：只输出 Unicode 仿字符，不能安装，免费但非真字体
- Fontself / Calligraphr：人工绘制/扫描转字体工具，质量可控但耗时以周计

## 情报判断

YoFont 踩中了「AI 生成字体」这个长期被 Unicode 仿字符工具占据、却鲜有真字体方案的空白，且用多书写系统（西里尔、阿拉伯、中日韩）建立了难以快速复制的壁垒。255.3K 的月增量很大程度上可能来自密集铺设的 SEO 长尾页与「首个免费」的低门槛，可持续性取决于生成质量能否留住付费用户（glyph 计量制意味着重度用户成本不低）。值得关注的点：API/MCP 接入 Claude Code、Cursor 等开发者工具，若能成为 Agent 工作流中的默认字体生成服务，天花板会明显高于纯 C 端工具。

---
*调研日期：2026-10-16 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
