---
title: Music Guessr
domain: musicguessr.io
---

# Music Guessr（musicguessr.io）

> GeoGuessr 式音乐国度猜谜日更游戏

## 产品是什么

Music Guessr 自称「GeoGuessr for Music」，是一个每日一局的网页猜谜游戏：玩家听 6 首歌曲片段，在世界地图上标记每位艺人的原籍国，按距离计分，满分 30,000。开发者/团队信息官网未披露，待核实。打开即玩，无需注册，音乐播放器内嵌在页面侧边栏中。

## 核心功能

- 每日 6 轮猜歌：每轮播放一段歌曲，猜测艺人来自哪个国家（来源：[官网](https://musicguessr.io/)）
- 世界地图点击作答，按地理距离计分，总分上限 30,000 分（来源：官网页面「Round 1/6」「0/30,000」）
- 内嵌音乐播放器，带播放按钮与进度条，浏览器内直接播放音频
- 纯网页免安装、免登录，打开即玩（Next.js 构建）
- SEO 定位为「daily music game / song geography game」，走 Wordle 式每日游戏路线（来源：官网 meta keywords）

## 流量表现

- 榜单数据：new 榜 rank 75，月访问量 26.9K，月增长 26.9K（即本月几乎全部流量为新增），首次被发现 2026-05-28。
- 增长可能原因（推测）：产品被收录进免费资源导航站 [fmhy.net（FreeMediaHeckYeah）游戏分区](https://fmhy.net/gaming)，此类导航站收录通常能带来稳定自然流量；此外「GeoGuessr + 音乐」的组合自带社交传播属性，契合每日游戏玩家分享成绩的传播路径。具体来源渠道待核实。

## 商业模式

未公开。官网未见定价页、付费功能或广告位，仅接入 Google Analytics，目前为纯免费产品，变现方式待核实。

## 竞争格局

- GeoGuessr：地理猜谜鼻祖，猜的是街景地点而非音乐，Music Guessr 是其玩法在音乐维度的衍生。
- MeloGuessr（meloguessr.com）：同为「猜歌曲原产国」玩法的地理音乐测验，5 轮制，功能高度重合。
- Heardle（已被 Spotify 关停）：曾经最火的每日猜歌游戏，猜歌名而非国家，证明了该品类需求，其关停留下用户空缺。
- Song Guessr（开源，GitHub）：多人对战的听歌猜歌游戏，偏社交聚会场景。

## 情报判断

Music Guessr 踩中了 Wordle 式每日小游戏的长尾红利：玩法一句话能讲清、零门槛免注册、成绩天然适合社交分享，获客成本极低。但此类产品壁垒薄、同质化严重（MeloGuessr 等几乎同玩法），且歌曲版权与音频来源是潜在合规风险点，能否持续取决于曲库更新与口碑传播，短期数据尚小，值得观察收录渠道带来的流量是否稳定。

---
*调研日期：2026-07-27 · 数据来源：[traffic.cv 榜单](https://traffic.cv/) + 官网 + 公开报道*
