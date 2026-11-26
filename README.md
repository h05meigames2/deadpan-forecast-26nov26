# Deadpan Forecast — Port Zedaria

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/h05meigames2/deadpan-forecast-26nov26/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/h05meigames2/deadpan-forecast-26nov26/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist"](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) ($2, winner-take-all).

## The forecast

> Tonight in Port Zedaria: 4°C, light drizzle, and a 90% chance the tide comes in twice, briefly, for reasons the harbourmaster declined to explain on air.

**153 characters** — one line, well within the 160-character limit.

## How it works

`main.ts` (Node 22) validates the line — exactly one line, 1–160 characters, not blank — then writes it to `/output/entry.txt`.

```bash
node main.ts
cat /output/entry.txt
```

## Why this one

Port Zedaria sounds like a real harbour town. The forecast opens like any TV bulletin (temperature, drizzle, a percentage), then lands one quiet absurdity — the tide coming in *twice* — delivered deadpan, with the harbourmaster refusing to explain on air. One twist, one concrete number, no padding.
