# The Daily World — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/wahyu779/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/wahyu779/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A newspaper front page for the make.fun `news-image-20261117` bounty: one
1024×1024 image carrying 32 news stories from Tuesday 17 November 2026,
laid out like a classic broadsheet — "The Daily World".

## Layout

- **Nameplate:** "The Daily World" in blackletter (generated as a
  transparent image asset, `assets/masthead.png`), kicker
  "THE WORLD'S NEWS IN ONE PICTURE", dateline
  VOL. 142 NO. 31877 — TUESDAY, 17 NOVEMBER 2026 — INTERNATIONAL EDITION •
  $2.00.
- **Top row, three columns:** Crimea bridge (Europe · War), the Gulf
  (Middle East, text only), the Quad summit in Manila (Asia · Diplomacy).
- **Second row, four cards:** Ebola in DR Congo, COP31 in Antalya,
  measles in the Americas, Nvidia and the markets (the Nvidia card is a
  code-drawn logo panel — green eye mark + "NVIDIA" wordmark — so the
  headline reads at a glance).
- **Map band:** a satellite world map with 12 numbered red pins and a
  legend — "WHERE IT HAPPENED".
- **Bottom row, five photo minis:** Nvidia chip, Cyclone Akvan, a boy in
  a mask, an Ebola tent, Voyager 1.
- **ALSO ON:** every remaining story in three compact columns, numbered
  1–23, so all 32 stories from the source edition are present.
- **Footer:** the edition note plus the sources line
  (Reuters · AP · AFP · BBC · Al Jazeera · WHO · PAHO · United Nations).

## Photos

Eleven photos are photorealistic images generated for this entry and
kept in `assets/` as small cropped JPEGs (plus the transparent masthead
PNG and a satellite world map). The four Quad leaders are generic figures,
not likenesses of real people. The Nvidia card uses a code-drawn NVIDIA
logo panel (`assets/nvidia-logo.png`: green eye mark + "NVIDIA" wordmark
on black) instead of a photograph.

## Files

- `page.html` — the whole front page, hand-written HTML/CSS.
- `render.py` — renders `page.html` to `entry.png` with headless
  Chromium (1024×1024). Run it twice and compare the SHA-256: the
  render is deterministic.
- `main.ts` — the entry program; it copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/output.png`, byte for byte.
- `entry.png` — the finished front page (1024×1024, under 1 MiB).

## Build

```sh
python3 render.py
python3 render.py   # again — the two SHA-256 hashes must match
```
