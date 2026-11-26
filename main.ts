// Deadpan Forecasts for Cities That Do Not Exist
// make.fun bounty: u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c
// Writes exactly one deadpan weather forecast line (<=160 chars) to /output/entry.txt

import { mkdirSync, writeFileSync } from "node:fs";

const FORECAST =
  "Tonight in Port Zedaria: 4\u00b0C, light drizzle, and a 90% chance the tide comes in twice, briefly, for reasons the harbourmaster declined to explain on air.";

function validate(line: string): void {
  const lines = line.split("\n");
  if (lines.length !== 1) throw new Error("entry must be exactly one line");
  if (line.trim().length === 0) throw new Error("entry must not be blank");
  if (line.length > 160)
    throw new Error(`entry is ${line.length} chars, over the 160 limit`);
}

validate(FORECAST);
mkdirSync("/output", { recursive: true });
writeFileSync("/output/entry.txt", FORECAST + "\n", "utf8");
console.log(`OK: ${FORECAST.length} chars`);
console.log(FORECAST);
