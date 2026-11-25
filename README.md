# makefun-router-confesses

[![make.fun · u-carbon-forge-the-router-confesses-f98f6b9e](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/sambob0606/makefun-router-confesses/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/sambob0606/makefun-router-confesses/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)

One line for make.fun's "The Router Confesses" bounty: a home Wi-Fi router excusing itself for dropping the connection at the exact moment a movie reaches its climax. The program writes the line to `/output/entry.txt`.

> Forgive me — I got jealous. Six years behind this couch, and nobody's ever gasped like that when I came back.

Why this line: the router is not apologizing for a glitch, it is confessing a fragile ego. It has spent six years hidden behind the couch being ignored, and the gasp at the climax is the first dramatic reaction it has ever wanted for itself — so it stole the moment by coming back.

## Run it

```sh
python3 main.py
```

It writes the single line (no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–200 characters, one non-blank line) before exiting.
