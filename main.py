"""News summary entry: writes a fixed summary of Wednesday 11 November 2026
to entry.txt. Deterministic: the same bytes on every run, no network.
The summary is 1,943 characters (limit 2,000); every fact was cross-checked
against Reuters, AFP, AP, the New York Times, Just Security and BTA."""

import os

SUMMARY = """World news, Wednesday 11 November 2026: US-mediated talks between Russia and Ukraine ended in Abu Dhabi after two days with agreement on the war's largest prisoner exchange, 1,000 or more a side, but no ceasefire, and Ukraine rejected Russian demands to surrender Donbas (Reuters). Russia struck six Ukrainian substations and a market in Chornomorsk, killing three, while Ukraine hit Russia's Ust-Luga oil port and NATO jets scrambled as drones strayed into Baltic airspace (Reuters). At COP31 in Antalya, UN chief Antonio Guterres told 102 leaders the slow climate response had put the world 'on a path to destruction' (AFP). US Secretary of State Marco Rubio said pressure on Iran was working and there was 'no need for major combat operations', as the Justice Department charged three Iran-backed operatives over nearly 20 alleged plots, including one at RAF Fairford (New York Times). Israeli forces killed at least seven people in Gaza, including a father and his 13-year-old son, health officials said, and Saudi Arabia said it intercepted seven Houthi missiles and drones aimed at Riyadh (Just Security). Ebola cases in the Democratic Republic of Congo passed 11,000 — 11,042 confirmed, 5,387 dead — the country's deadliest outbreak, its health ministry said (Reuters). October US inflation came in hot, with prices up 0.4% and core prices up 0.3%, pushing the 10-year Treasury yield towards 5% and raising December rate-rise expectations; the Nasdaq gained 1.6% (Reuters). House Republicans blocked an effort to impeach Defense Secretary Pete Hegseth, and Democrat Scott Colom won Mississippi's US Senate seat, the Associated Press called. British police arrested a 41-year-old US Army officer on suspicion of spying for Russia, and the UK's top court struck down Trinidad and Tobago's colonial-era ban on gay sex (Just Security). Bulgaria observed a day of mourning after a fog pile-up on the Trakia motorway killed at least 11 (BTA)."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SUMMARY)
