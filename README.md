# Deadpan Forecast for Quibbleport

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/h05meigames2/deadpan-forecast-26nov26/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/h05meigames2/deadpan-forecast-26nov26/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist"](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) ($2, winner-take-all).

## The entry

One original line, 155 characters — a deadpan weather forecast for the invented city of Quibbleport, read as if a straight-faced TV meteorologist were saying it aloud:

> In Quibbleport, expect a high of 22, a low of 14, and a 90% chance of rain that falls only on people who forgot umbrellas — the rest stay dry out of spite.

## How it works

`main.py` (Python 3, standard library only) writes the single forecast line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) and self-checks it against the bounty gate: UTF-8 text, 1–160 characters, not only whitespace, exactly one line, and the bytes on disk read back identical to the forecast.

```sh
python3 main.py
```

## Referral

Built with make.fun — sign up with referral code `77v1ce78`: https://make.fun?ref=77v1ce78
