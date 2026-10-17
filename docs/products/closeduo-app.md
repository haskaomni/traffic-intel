---
title: CloseDuo
domain: closeduo.app
---

# CloseDuo（closeduo.app）

> 把折叠屏手机开合动画搬上 MacBook 的小工具

## 产品是什么

CloseDuo 是一款 macOS 菜单栏小工具，把 viral 的「iPhone Duo」折叠屏开机动画复刻到 MacBook 上：打开或合拢上盖时，桌面内容会随转轴角度实时倾斜、模糊、淡出。它直接读取 Mac 自带的转轴角度传感器（lid angle sensor），用 Metal 渲染捕获的桌面画面，窗口和壁纸联动。售价 $3.99 买断（[官网](https://closeduo.app/)）。开发者身份未在官网署名，待核实。

## 核心功能

- 读取 Mac 转轴角度传感器驱动动画，官方称「无轮询、无辅助功能 hack」（[官网](https://closeduo.app/)）
- 实时捕获桌面并用 Metal 渲染倾斜/模糊效果
- 三种预设风格：Silk、Shade、Frost，可自定义透视、模糊、阴影及清除角度
- 0.3 版新增开盖时的轻触音效，可关闭
- 常驻菜单栏，点击或按 Esc 暂停
- 本地处理、无账号体系，承诺不录制不上传屏幕内容

## 流量表现

- 榜单数据：new 榜 rank 37，月访问量 53.8K，月增长 53.8K（即几乎全部流量为当月新增），首次被发现 2026-09-11。
- 增长背景：2026 年 9 月初「iPhone Duo」折叠开合动画在网上走红，多位开发者在一周内推出 Mac 版复刻并互相借势传播——9 月 10 日前后 GitHub 出现 [Mac-Duo](https://github.com/sumimakito/Mac-Duo)、[iphone-duo-macos-animation](https://github.com/lqSky7/iphone-duo-macos-animation) 等开源实现，[Macworld 于 2026-09-11 报道](https://www.macworld.com/article/3233434/that-amazing-iphone-duo-open-animation-has-already-come-to-the-macbook.html)了这股风潮，另有 [Bendy（$4.99，开发者 Adrian Belarde）](https://www.facebook.com/100083241103501/videos/1702570894164910/) 等付费竞品。CloseDuo 首次被发现日期（2026-09-11）恰好落在话题峰值期，其 53.8K 月访问几乎可全部归因于这波热点（推测）。

## 商业模式

买断制：$3.99 一次付费，DMG 下载，许可密钥邮件发送，最多可在 3 台 Mac 上使用（[官网](https://closeduo.app/)）。无订阅、无免费版（竞品中有免费开源替代品）。变现规模有限，属典型独立开发者小工具模式。

## 竞争格局

- [Mac Duo](https://github.com/sumimakito/Mac-Duo)：免费开源，功能相近，直接分流付费意愿。
- [Bendy](https://x.com/i/trending/2098057761577914691)：Adrian Belarde 开发的付费版（$4.99），定价略高，同期借势营销。
- [iphone-duo-macos-animation](https://github.com/lqSky7/iphone-duo-macos-animation)：免费 Swift 原生开源克隆，技术实现透明。
- CloseDuo 的差异点在于三种风格预设 + 音效 + 成品化包装，但护城河极浅。

## 情报判断

CloseDuo 是典型的「热点套利」型微产品：蹭上 iPhone Duo 动画的 viral 话题，用极低成本快速上线收割好奇心流量。$3.99 买断定价适合冲动消费，但免费开源替代品众多，且话题热度天然短周期，53.8K 月访问大概率在热点退潮后快速回落，可持续性弱。值得关注的不是产品本身，而是这类「围绕 Apple 传闻/热点快速出货」的独立开发者打法。

---
*调研日期：2026-10-18 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
