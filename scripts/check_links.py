#!/usr/bin/env python3
"""Check paper and code URLs concurrently without third-party dependencies."""
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf-8"))


def check(item):
    paper_id, kind, url = item
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 AI-Agent-Security-Papers link checker"})
    try:
        with urlopen(request, timeout=15) as response:
            return paper_id, kind, url, response.status, ""
    except HTTPError as exc:
        # 403/429 normally means the host rejected automation, not that the link is missing.
        if exc.code in {403, 405, 429}:
            return paper_id, kind, url, exc.code, "automation blocked"
        return paper_id, kind, url, exc.code, str(exc)
    except (URLError, TimeoutError) as exc:
        return paper_id, kind, url, 0, str(exc)


items = []
for paper in PAPERS:
    items.append((paper["id"], "paper", paper["paper_url"]))
    if paper["code_url"]:
        items.append((paper["id"], "code", paper["code_url"]))

failed = []
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(check, item) for item in items]
    for future in as_completed(futures):
        result = future.result()
        paper_id, kind, url, status, note = result
        print(f"{status:>3} {kind:<5} {paper_id}: {url}{' (' + note + ')' if note else ''}")
        if status == 0 or status == 404 or status >= 500:
            failed.append(result)

if failed:
    raise SystemExit(f"Broken or unreachable links: {len(failed)}")
print(f"Checked {len(items)} links; no confirmed broken links.")
