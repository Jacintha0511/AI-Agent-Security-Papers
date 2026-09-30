#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = json.loads((ROOT / "taxonomy" / "regex_rules.json").read_text(encoding="utf-8"))


def classify(text: str):
    hits = []
    for rank, rule in enumerate(RULES):
        matches = re.findall(rule["pattern"], text)
        if matches:
            hits.append({"category": rule["category"], "matches": len(matches), "precedence": rank})
    return sorted(hits, key=lambda x: (-x["matches"], x["precedence"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Suggest primary categories using repository regex rules.")
    parser.add_argument("text", help="Paper title, abstract, or keywords")
    args = parser.parse_args()
    print(json.dumps(classify(args.text), ensure_ascii=False, indent=2))
