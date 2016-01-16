# FantasyLCS-Python-API

### Requirements
- Requests
- Arrow
- Tabulate (for examples)


### Examples
[Match Schedule](https://github.com/0Zaga0/FantasyLCS-Python-API/blob/master/examples/match_schedule.py)
<pre>
Week    Date              Blue Team             Red Team              Completed
------  ----------------  --------------------  --------------------  -----------
Week 1  Jan 14, 11:00 AM  Origen                Fnatic                Y
Week 1  Jan 14, 12:00 PM  G2 Esports            Elements              Y
Week 1  Jan 14, 1:00 PM   Giants                H2K                   Y
Week 1  Jan 14, 2:00 PM   Unicorns of Love      Splyce                Y
Week 1  Jan 14, 3:00 PM   ROCCAT                Vitality              Y
Week 1  Jan 15, 11:00 AM  Unicorns of Love      Giants                Y
Week 1  Jan 15, 12:00 PM  Elements              Splyce                Y
Week 1  Jan 15, 1:00 PM   Fnatic                Vitality              Y
Week 1  Jan 15, 2:00 PM   Origen                H2K                   Y
Week 1  Jan 15, 3:00 PM   ROCCAT                G2 Esports            Y
Week 1  Jan 16, 2:00 PM   Counter Logic Gaming  TSM                   N
Week 1  Jan 16, 3:00 PM   Immortals             Cloud9                N
...
</pre>

[Player Stats Table](https://github.com/0Zaga0/FantasyLCS-Python-API/blob/master/examples/player_stats_table.py)
<pre>
Name            Matches Played    K    D    A    CS    2x    3x    4x    5x    10+ K/A
------------  ----------------  ---  ---  ---  ----  ----  ----  ----  ----  ---------
Adrian                       0    0    0    0     0     0     0     0     0          0
Adryh                        2    4    3    4   526     0     0     0     0          0
Airwaks                      2    4    4    7   297     0     0     0     0          0
Alex Ich                     0    0    0    0     0     0     0     0     0          0
Altec                        0    0    0    0     0     0     0     0     0          0
Amazing                      2    2    7    9   219     0     0     0     0          0
aphromoo                     0    0    0    0     0     0     0     0     0          0
Apollo                       0    0    0    0     0     0     0     0     0          0
Atom                         2    2    6    6   420     0     0     0     0          0
Balls                        0    0    0    0     0     0     0     0     0          0
beibei                       0    0    0    0     0     0     0     0     0          0
BetongJocke                  0    0    0    0     0     0     0     0     0          0
Betsy                        2    5    3    6   478     0     0     0     0          0
Big                          0    0    0    0     0     0     0     0     0          0
...
</pre>

[Team Stats Table](https://github.com/0Zaga0/FantasyLCS-Python-API/blob/master/examples/team_stats_table.py)
<pre>
Name                    Matches Played    W    L    Secs Played    1st B    Tw    Dr    Ba    <30m W
--------------------  ----------------  ---  ---  -------------  -------  ----  ----  ----  --------
Cloud9                               0    0    0              0        0     0     0     0         0
Counter Logic Gaming                 0    0    0              0        0     0     0     0         0
Echo Fox                             0    0    0              0        0     0     0     0         0
Elements                             2    1    1           3464        2    10     3     1         0
Fnatic                               2    1    1           3815        0    13     3     1         0
G2 Esports                           2    2    0           3004        0    20     3     2         2
Giants                               2    0    2           3831        1     6     1     0         0
H2K                                  2    2    0           3242        1    20     2     2         2
Immortals                            0    0    0              0        0     0     0     0         0
Liquid                               0    0    0              0        0     0     0     0         0
NRG Esports                          0    0    0              0        0     0     0     0         0
Origen                               2    0    2           3859        1     2     3     0         0
Renegades                            0    0    0              0        0     0     0     0         0
ROCCAT                               2    1    1           3546        2    15     3     1         0
Splyce                               2    0    2           3515        0     7     0     0         0
Team Dignitas                        0    0    0              0        0     0     0     0         0
Team Impulse                         0    0    0              0        0     0     0     0         0
TSM                                  0    0    0              0        0     0     0     0         0
Unicorns of Love                     2    2    0           3907        2    20     5     3         1
Vitality                             2    1    1           3765        1    15     4     1         1
</pre>
