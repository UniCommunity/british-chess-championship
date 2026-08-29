#!/usr/bin/env python3
"""Query data/championships.json"""
import argparse, json
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--year", type=int)
    p.add_argument("--player")
    p.add_argument("--venue")
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / "data" / "championships.json").read_text())
    rows = data["records"]
    if args.year:
        rows = [r for r in rows if r["year"] == args.year]
    if args.player:
        q = args.player.lower()
        rows = [r for r in rows if any(q in n.lower() for n in r["open_champions"] + r["women_champions"])]
    if args.venue:
        q = args.venue.lower()
        rows = [r for r in rows if (r.get("venue") or "").lower().find(q) >= 0]
    print(json.dumps(rows, indent=2, ensure_ascii=False))
    print(f"\n# {len(rows)} row(s)")

if __name__ == "__main__":
    main()
