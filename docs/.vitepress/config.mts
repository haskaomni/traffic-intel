import { defineConfig } from 'vitepress'
import { readFileSync, existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const root = join(dirname(fileURLToPath(import.meta.url)), '..', '..')

// 从 data/products.json 生成产品报告侧边栏（按收录日期倒序）
function productSidebar() {
  const file = join(root, 'data', 'products.json')
  if (!existsSync(file)) return []
  const data = JSON.parse(readFileSync(file, 'utf-8'))
  return data.products
    .filter((p) => p.report)
    .sort((a, b) => (b.added || '').localeCompare(a.added || ''))
    .map((p) => ({
      text: p.title || p.domain,
      // 文件名 slug 化：点号会让 Pages 误判扩展名导致 404
      link: `/products/${p.domain.replaceAll('.', '-')}`,
    }))
}

export default defineConfig({
  lang: 'zh-CN',
  title: 'Traffic 新品情报',
  description: '监控 traffic.cv 流量榜单，每日自动调研新跑出来的产品。',
  base: '/traffic-intel/',
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '产品总览', link: '/products/' },
      { text: '监控说明', link: '/boards' },
    ],
    sidebar: {
      '/products/': [
        {
          text: '产品报告',
          items: [{ text: '总览', link: '/products/' }, ...productSidebar()],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/haskaomni/traffic-intel' },
    ],
    footer: {
      message: '榜单数据来自 traffic.cv · 由智能体每日自动调研更新',
    },
    outline: { label: '本页目录' },
    lastUpdatedText: '最后更新',
  },
})
