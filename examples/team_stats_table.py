__author__ = 'John Sabath'

from tabulate import tabulate
from fantasylcs import FantasyLCS

fantasy_lcs = FantasyLCS(season_id=12)
fantasy_lcs.load()

table = []
for team in fantasy_lcs.get_teams():
    stats = team.get_season_stats()
    row = [
        team.get_name(),
        stats['matchesPlayed']['actual'],
        stats['matchVictory']['actual'],
        stats['matchDefeat']['actual'],
        stats['secondsPlayed']['actual'],
        stats['firstBlood']['actual'],
        stats['towerKills']['actual'],
        stats['dragonKills']['actual'],
        stats['baronKills']['actual'],
        stats['quickWinBonus']['actual'],
    ]
    table.append(row)

table.sort(key=lambda x: x[0].lower())

print(tabulate(table, headers=["Name", "Matches Played", "W", "L", "Secs Played", "1st B", "Tw", "Dr", "Ba", "<30m W"]))