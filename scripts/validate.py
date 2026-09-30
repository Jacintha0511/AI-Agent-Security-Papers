#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf-8"))
RULES = json.loads((ROOT / "taxonomy" / "regex_rules.json").read_text(encoding="utf-8"))
CATEGORIES = {r["category"] for r in RULES}
REQUIRED = {"id", "title", "title_zh", "year", "venue", "status", "category", "tags", "paper_url", "code_url", "why_zh", "why_en", "contributions_zh", "contributions_en"}

errors = []
seen_ids, seen_urls = set(), set()
for index, p in enumerate(PAPERS, 1):
    missing = REQUIRED - set(p)
    if missing:
        errors.append(f"#{index} missing fields: {sorted(missing)}")
        continue
    if p["id"] in seen_ids:
        errors.append(f"duplicate id: {p['id']}")
    seen_ids.add(p["id"])
    if p["paper_url"] in seen_urls:
        errors.append(f"duplicate paper URL: {p['paper_url']}")
    seen_urls.add(p["paper_url"])
    if p["category"] not in CATEGORIES:
        errors.append(f"{p['id']}: unknown category {p['category']}")
    if p["status"] not in {"peer-reviewed", "preprint"}:
        errors.append(f"{p['id']}: invalid status")
    if len(p["contributions_zh"]) != 3 or len(p["contributions_en"]) != 3:
        errors.append(f"{p['id']}: each language must contain exactly three contributions")
    for key in ("paper_url", "code_url"):
        value = p[key]
        if value and urlparse(value).scheme not in {"http", "https"}:
            errors.append(f"{p['id']}: invalid {key}")
    if not re.fullmatch(r"[a-z0-9-]+", p["id"]):
        errors.append(f"{p['id']}: id must be lowercase kebab-case")

for name in ("README.md", "README_CN.md"):
    path = ROOT / name
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if text.count("### ") != len(PAPERS):
            errors.append(f"{name}: expected {len(PAPERS)} paper cards, found {text.count('### ')}")

if len(PAPERS) != 30:
    errors.append(f"expected 30 papers, found {len(PAPERS)}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validation passed: {len(PAPERS)} papers, {len(CATEGORIES)} categories, bilingual contributions complete.")
