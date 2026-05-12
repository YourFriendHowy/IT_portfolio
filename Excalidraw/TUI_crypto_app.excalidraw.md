---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Linegraph ^S81MbTlB

Table showing time based snapshots
Deviation from principal (the red/green %)
Pincliple to current value percentage, anything above thresh hold in blue to notify potential sell 
 ^UsmlWqG6

investment goal with progress bar ^a8aVKBst

Total profit/loss ^8YdvlT3q

Per coin profit/loss ^nWR3fhJL

Current Value ^k3Uej887

Principle ^7rf0n4MV

transaction feed, shows last
X amount of deposits based
on terminal size

Make the top level
Purchase expandable
give it a keybind to drop
down each menu, total 20. 

example:
 ^48tMTSQP

▼Bought $X USDC
    $x btc
    $x Eth
    $cont listing what was 
        bought with USDC  ^6TCKs61A

so heres the function idea, the top level goes by date 
so everything that is purchased on the same date
after the time stamp goes under that top level.
USDC is the trigger to consolidate, and only for the first
buy per coin within an hour of the usdc being purchased!
everything else is a single transaction, we will
do buy and sells, colors are orange for buy, purple for sale,
it will be a limited feed with a keybind to
open a full panel that is scrollable and covers the past 3 
months of transactions or 100 which ever is less. ^GfNgNC7J

▼ 2025-01-14 | Bought $500 USDC
    $150 BTC   — orange
    $100 ETH   — orange
    $100 SOL   — orange

▼ 2025-01-15 | Bought $300 USDC
    $300 BTC   — orange

● 2025-01-16 | Sold $40 DOGE    — purple
● 2025-01-17 | Bought $50 BTC   — orange ^3v0AdejS

==============================================================
OVERVIEW MODE
==============================================================

Top left:   Investment goal + progress bar
            toward $30k handoff threshold
Top right:  Total P/L in dollars and percent
Mid left:   Portfolio line graph
            all coins, full history
Mid right:  Per coin P/L — short term
            1hr / 4hr / 12hr / 24hr snapshots
Bot left:   Snapshot table (default)
            OR bar graph (toggle v)
            Deviation from principal red/green
            Threshold alerts in blue
Bot right:  Deposit feed tree — grouped by date
            USDC purchases consolidate children
            within 1hr window
            +$X appended if multiple USDC same day
            Limited view with keybind to full panel
            3 months or 100 transactions

==============================================================
SINGLE COIN MODE
==============================================================

Top left:   Investment goal + progress bar
            (unchanged)
Top right:  Total P/L (unchanged)
Mid left:   Selected coin line graph only
Mid right:  Selected coin P/L — zoomed out
            1month / 3month / 6month / 1year
Bot left:   Live price feed, ticking real time
Bot right:  Selected coin transactions only
            Buys orange, sells purple

==============================================================
NAV
==============================================================

Top bar coin selector
Keybinds switch between overview and single coin
Top left and top right always persist unchanged

==============================================================
TABLE PANEL CONTROLS
==============================================================

Ctrl+1-9     Cycles through coins
             Only bottom left table panel updates
             Everything else stays in overview
Ctrl+0 / Esc Snaps back to overview snapshot table
t            Cycles timeframe:
               24hr   — 1hr averages,   24 rows
               1week  — 4hr averages,   42 rows
               1month — daily averages, 30 rows

All timeframe views are scrollable
Panel header: [BTC | 24hr] or [Overview | Snapshot]

==============================================================
GLOBAL
==============================================================

Percentages displayed to .00
Red/green deviation colors throughout
Blue highlight on anything above sell threshold
Buys orange, sells purple throughout all views
Expandable deposit tree with v / > toggle
Full transaction panel keybind
  3 months or 100 transactions, whichever is less
Daemon runs separately from TUI
  — Per coin poll intervals
      60s meme coins, 5min stable coins
  — Discord webhooks for threshold alerts
  — Hourly summary table to Discord ^BoviGBIU

%%
## Drawing
```compressed-json
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
```
%%