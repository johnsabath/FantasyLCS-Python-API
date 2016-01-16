__author__ = 'John Sabath'

from tabulate import tabulate
from fantasylcs import FantasyLCS

fantasy_lcs = FantasyLCS(season_id=12)
fantasy_lcs.load()

table = []
for player in fantasy_lcs.get_players():
    stats = player.get_season_stats()
    row = [
        player.get_name(),
        stats['matchesPlayed']['actual'],
        stats['kills']['actual'],
        stats['deaths']['actual'],
        stats['assists']['actual'],
        stats['minionKills']['actual'],
        stats['doubleKills']['actual'],
        stats['tripleKills']['actual'],
        stats['quadraKills']['actual'],
        stats['pentaKills']['actual'],
        stats['killOrAssistBonus']['actual'],
    ]
    table.append(row)

table.sort(key=lambda x: x[0].lower())

print(tabulate(table, headers=["Name", "Matches Played", "K", "D", "A", "CS", "2x", "3x", "4x", "5x", "10+ K/A"]))