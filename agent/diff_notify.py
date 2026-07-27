#!/usr/bin/env python3
"""diff_notify.py — 比较快照与当前 data/products.json，输出 TG 通知文案。

用法: diff_notify.py <快照目录（含 products.json）>
无新增报告 / 新上榜域名时不输出任何内容（退出码 0）。
"""
import datetime
import json
import sys

SNAP = sys.argv[1]
DATA = "data/products.json"
SITE = "https://haskaomni.github.io/traffic-intel/"


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


before = {p["domain"]: p for p in (load(f"{SNAP}/products.json") or {}).get("products", [])}
after = (load(DATA) or {}).get("products", [])

new_domains = [p["domain"] for p in after if p["domain"] not in before]
new_reports = [
    (p["title"] or p["domain"], p["domain"])
    for p in after
    if p.get("report") and not before.get(p["domain"], {}).get("report")
]

if not new_domains and not new_reports:
    sys.exit(0)

lines = [f"Traffic 情报 · {datetime.date.today().isoformat()} 更新"]
if new_reports:
    lines.append(f"新增产品报告 {len(new_reports)} 篇：")
    lines += [f"• {t} ({d})" for t, d in new_reports[:8]]
if new_domains:
    lines.append(f"新上榜域名 {len(new_domains)} 个：" + "、".join(new_domains[:8]))
lines.append(SITE)
print("\n".join(lines))
