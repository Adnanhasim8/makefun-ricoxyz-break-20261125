[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Adnanhasim8/makefun-ricoxyz-break-20261125/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Adnanhasim8/makefun-ricoxyz-break-20261125/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

Entry for the make.fun competition `u-ricoxyz-break-production-own-it-be78a994`.

The program writes one brutally honest single-line error message — the line an AI agent prints the instant it breaks production — to `/output/entry.txt`:

> I ran DROP DATABASE in the wrong terminal. The right one is still open. The database is not.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13 standard library only, no network. The program asserts its own gate before writing: the output is exactly one line of 1–200 characters.
