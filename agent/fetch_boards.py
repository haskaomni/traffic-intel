#!/usr/bin/env python3
"""fetch_boards.py — 抓取 traffic.cv 本月 traffic 榜单（new / trending），更新 data/products.json。

- 榜单每月 10 日左右更新上个月的数据；自动从当月开始向前找最新非空月份。
- 免费层每榜可见 12 条（其余为 Pro 打码行），只解析可见行。
- 新出现的域名追加到 products.json（report=null，等待智能体调研）；
  已有域名只刷新 rank / visits / growth / boards。

用法: python3 agent/fetch_boards.py
"""
import datetime
import html as html_mod
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PRODUCTS = DATA / "products.json"
BOARDS = ("new", "trending")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
NUM = re.compile(r"^[\d.]+[KMB]?$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def parse_board(html):
    """从榜单 HTML 解析可见行：rank / domain / visits / growth / first_seen / desc。"""
    rows = []
    for li in re.findall(r'<li class="lb-rise".*?</li>', html, re.S):
        m = re.search(r'href="/([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)"', li)
        if not m:
            continue  # Pro 打码行没有域名链接
        domain = m.group(1).lower()
        txt = html_mod.unescape(re.sub(r"<[^>]+>", "|", li))
        parts = [p.strip() for p in re.sub(r"\|+", "|", txt).split("|") if p.strip()]
        try:
            di = parts.index(domain)
        except ValueError:
            continue
        rank = int(parts[0]) if parts and parts[0].isdigit() else None
        # 域名之后：可选描述文本，随后是 visits、▲/▼、增长量、first_seen
        tail = parts[di + 1:]
        desc_parts = []
        while tail and not NUM.match(tail[0]):
            desc_parts.append(tail.pop(0))
        nums = [t for t in tail if NUM.match(t)]
        first_seen = next((t for t in tail if DATE.match(t)), None)
        rows.append({
            "rank": rank,
            "domain": domain,
            "visits": nums[0] if nums else None,
            "growth": nums[1] if len(nums) > 1 else None,
            "first_seen": first_seen,
            "desc": " ".join(desc_parts) or None,
        })
    # 去重（桌面 / 移动两套标记可能各出现一次）
    seen, out = set(), []
    for r in rows:
        if r["domain"] not in seen:
            seen.add(r["domain"])
            out.append(r)
    return out


def latest_month():
    """从当月开始向前找最新非空榜单月份，返回 (month_str, {board: rows})。"""
    today = datetime.date.today()
    y, m = today.year, today.month
    for _ in range(4):
        month = f"{y}-{m:02d}"
        boards = {}
        for b in BOARDS:
            url = f"https://traffic.cv/leaderboard/traffic/{y}/{m}/{b}"
            try:
                rows = parse_board(fetch(url))
            except Exception as e:
                print(f"  抓取失败 {url}: {e}")
                rows = []
            boards[b] = rows
        if any(boards.values()):
            return month, boards
        print(f"  {month} 榜单为空，回退上一月")
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return None, {b: [] for b in BOARDS}


def main():
    today = datetime.date.today().isoformat()
    month, boards = latest_month()
    if not month:
        print("未找到任何非空榜单")
        return
    total = sum(len(v) for v in boards.values())
    print(f"榜单月份 {month}：new {len(boards['new'])} 条，trending {len(boards['trending'])} 条")

    registry = {"month": month, "fetched": today, "products": []}
    if PRODUCTS.exists():
        registry = json.loads(PRODUCTS.read_text(encoding="utf-8"))
    registry["month"] = month
    registry["fetched"] = today
    by_domain = {p["domain"]: p for p in registry["products"]}

    added = []
    for board, rows in boards.items():
        for r in rows:
            p = by_domain.get(r["domain"])
            if p is None:
                p = {
                    "domain": r["domain"],
                    "boards": [],
                    "rank": {},
                    "visits": None,
                    "growth": None,
                    "first_seen": r["first_seen"],
                    "board_desc": r["desc"],
                    "added": today,
                    "report": None,
                    "title": None,
                    "summary": None,
                    "category": None,
                }
                registry["products"].append(p)
                by_domain[r["domain"]] = p
                added.append(r["domain"])
            if board not in p["boards"]:
                p["boards"].append(board)
            p["rank"][board] = r["rank"]
            p["visits"] = r["visits"]
            p["growth"] = r["growth"]
            if r["first_seen"]:
                p["first_seen"] = r["first_seen"]
            if r["desc"]:
                p["board_desc"] = r["desc"]

    DATA.mkdir(exist_ok=True)
    PRODUCTS.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    pending = [p["domain"] for p in registry["products"] if not p["report"]]
    print(f"注册表共 {len(registry['products'])} 个域名；本次新上榜 {len(added)} 个: {added}")
    print(f"待调研（无报告）: {len(pending)} 个: {pending}")


if __name__ == "__main__":
    main()
