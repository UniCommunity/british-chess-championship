# British Chess Championship dataset

Compiled roll of the **British Chess Championship** modern series (1904–2026), plus cancelled and non-title years.

Repo: https://github.com/UniCommunity/british-chess-championship

## Current champions (2026, Coventry)

- Open: **GM Shreyas Royal** (7.5/9) — youngest British Champion on record (17)
- Women: **FM Bodhana Sivanandan** — youngest British Women’s Champion on record (11), after a rapid play-off with WGM Trisha Kanyamarala

## Files

| File | Use |
| --- | --- |
| `data/championships.csv` | One row per year — the main database |
| `data/recent_events.json` | Extra detail for 2024–2026 |
| `scripts/query.py` | Filter the CSV by year, player, or venue |

CSV columns: `edition,year,venue,status,open_champions,women_champions,notes`

`status` is one of:

- `held` — open title awarded
- `no_open_title` — congress existed but the open British title was not at stake
- `cancelled` — no championship (wars, 2020 pandemic)

Shared titles are joined with ` | `.

## Query examples

```bash
python3 scripts/query.py --year 2026
python3 scripts/query.py --player "Michael Adams"
python3 scripts/query.py --venue Hull
```

## Scope and limits

- This is **not** an official ECF product. Official prize lists: https://www.britishchesschampionships.co.uk/
- Historical names follow [BritBase](https://www.saund.co.uk/britbase/britchamps.html) (John Saunders), last checked 12 August 2026.
- Pre-1904 BCA Challenge Cup winners (1866–1872) are not in the main table: Cecil De Vere (1866), Joseph Henry Blackburne (1869), John Wisker (1870, 1872).
- Junior / senior sections are not fully enumerated here.

## Sources

- BritBase champion list: https://www.saund.co.uk/britbase/britchamps.html
- ECF 2024 results: https://www.englishchess.org.uk/2024-british-chess-championship-results/
- Official 2025 winners: https://www.britishchesschampionships.co.uk/2025-results-and-winners-page/
- ECF 2026 wrap: https://www.englishchess.org.uk/the-2026-british-chess-championships-conclude-in-coventry/
