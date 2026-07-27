#!/usr/bin/env python3
"""build_index.py — 从 data/products.json 生成 docs/products/index.md 总览页。

数据与展示分离：智能体只维护 data/products.json 与 docs/products/<domain-slug>.md，
本脚本负责渲染产品总览表（类似 ai-game-intel 的 build.py 角色）。
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "products.json"
OUT = ROOT / "docs" / "products" / "index.md"


def main():
    d = json.loads(DATA.read_text(encoding="utf-8"))
    products = sorted(d["products"], key=lambda p: p["added"], reverse=True)

    lines = [
        "---",
        "title: 产品总览",
        "---",
        "",
        "# 产品总览",
        "",
        f"跟踪榜单：**{d['month']}** traffic 榜（new / trending），"
        f"共收录 {len(products)} 个产品，最近抓取：{d['fetched']}。",
        "",
        "| 产品 | 榜单 | 排名 | 月访问量 | 月增长 | 首次发现 | 报告 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for p in products:
        boards = " / ".join(p["boards"])
        ranks = " / ".join(f"#{p['rank'][b]}" for b in p["boards"] if b in p["rank"])
        title = p["title"] or p["domain"]
        if p["report"]:
            slug = p["domain"].replace(".", "-")
            name = f"[{title}](./{slug})"
            report = "✅"
        else:
            name = title
            report = "调研中"
        lines.append(
            f"| {name} | {boards} | {ranks} | {p['visits'] or '—'} "
            f"| {p['growth'] or '—'} | {p['first_seen'] or '—'} | {report} |"
        )
    lines += [
        "",
        "::: tip 数据来源",
        "榜单数据来自 [traffic.cv](https://traffic.cv/) 每月 survey（建模估计值，"
        "非 analytics 导出），免费层每榜可见前 12 个未打码条目。",
        ":::",
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"built {OUT} ({len(products)} 个产品)")


if __name__ == "__main__":
    main()
