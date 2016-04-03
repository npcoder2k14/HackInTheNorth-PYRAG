# HackInTheNorth-PYRAG
Sports API
# Installing Command line tool for pyrag
You must have python3 installed on your local system.
Download the [zip](https://github.com/npcoder2k14/HackInTheNorth-PYRAG/archive/dev.zip) file or clone the repository dev's branch
```bash
$ git clone https://github.com/npcoder2k14/HackInTheNorth-PYRAG/tree/dev
```
Install the requirements
```bash
$ pip install -r requirements.txt
```
Run setup.py
```bash
$ python setup.py install
```
# Usage
```bash
$ pyrag -h
Usage: sport-api [-h] [-F] [-C] live_score|news|[player_stats name] [-my_fav_team]

Get latest updates for football and cricket

Options:

-h, --help                shows help(this) message

-F, --football [uefa,
barclay, fifa]            Get football updates. The tournament for which you
                          want to get updates. One of the argumets from uefa,
                          barclay and fifa is compulsory.

-C, --cricket             Get cricket updates for international matches.

[live-score, news,
,fixtures
player-stats[name]]       Fields to get. `live-scores` to get live socre of
                          on-going matches, `news` to get latest news headlines,
                          `player-stats` to get statistics of player specified.
                          `fixtures` to get updates on upcoming messages.
                          Compulsory single argument. For football option you
                          can give additional options topscorer.
                          Use `-` instead of space in names.

-proxy                    To specify proxy. Defaults to system proxy. Take name of
                          a file. Sample -proxy http://username:password@host:port/

$ pyrag -F barclay topscorer
╒══════════════════╤═══════════════╕
│ Player Name      │   Goal Scored │
╞══════════════════╪═══════════════╡
│ Diego Costa      │            11 │
├──────────────────┼───────────────┤
│ Harry Kane       │            22 │
├──────────────────┼───────────────┤
│ Romelu Lukaku    │            18 │
├──────────────────┼───────────────┤
│ Gylfi Sigurdsson │            10 │
├──────────────────┼───────────────┤
│ Jamie Vardy      │            19 │
├──────────────────┼───────────────┤
│ Sergio Agüero    │            17 │
├──────────────────┼───────────────┤
│ Jermain Defoe    │            12 │
├──────────────────┼───────────────┤
│ Olivier Giroud   │            12 │
├──────────────────┼───────────────┤
│ Riyad Mahrez     │            16 │
├──────────────────┼───────────────┤
│ Odion Ighalo     │            14 │
╘══════════════════╧═══════════════╛
```


