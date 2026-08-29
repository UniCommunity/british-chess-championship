#!/usr/bin/env python3
"""Query data/championships.csv"""
import argparse, csv, json
from pathlib import Path

def load():
    root = Path(__file__).resolve().parents[1]
    rows = []
    with (root / "data" / "championships.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({
                "edition": int(r["edition"]) if r["edition"] else None,
                "year": int(r["year"]),
                "venue": r["venue"] or None,
                "status": r["status"],
                "open_champions": [x.strip() for x in r["open_champions"].split("|") if x.strip()],
                "women_champions": [x.strip() for x in r["women_champions"].split("|") if x.strip()],
                "notes": r["notes"] or None,
            })
    return rows

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--year", type=int)
    p.add_argument("--player")
    p.add_argument("--venue")
    args = p.parse_args()
    rows = load()
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
