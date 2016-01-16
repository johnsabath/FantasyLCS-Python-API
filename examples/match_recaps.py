__author__ = 'John'

from fantasylcs import FantasyLCS
from tabulate import tabulate

fantasy_lcs = FantasyLCS(season_id=12)
fantasy_lcs.load()

for match in fantasy_lcs.get_matches():
    if not match.is_completed():
        continue

    blue_team = match.get_blue_team()
    blue_players = match.get_player_stats(blue_team.get_id())

    red_team = match.get_red_team()
    red_players = match.get_player_stats(red_team.get_id())

    table1 = []
    for team in (blue_team, red_team):
        stats = team.get_single_match_stats(match.get_id())
        table1.append([
            team.get_name(),
            "X" if stats['matchVictory']['actual'] else "",
            "X" if stats['quickWinBonus']['actual'] else "",
            "X" if stats['firstBlood']['actual'] else "",
            stats['towerKills']['actual'],
            stats['dragonKills']['actual'],
            stats['baronKills']['actual']
        ])
    print(tabulate(table1, headers=['Name', 'Win', 'Quick Win', '1st Blood', 'Tw', 'Dr', 'Ba']))
    print("")

    table2 = []
    for players in [blue_players, None, red_players]:
        # Spacing between blue team players and red team players
        if players is None:
            table2.append(" "*9)
            continue

        for player, stats in players:
            table2.append([
                player.get_name(),
                stats['kills']['actual'],
                stats['deaths']['actual'],
                stats['assists']['actual'],
                stats['minionKills']['actual'],
                stats['tripleKills']['actual'],
                stats['quadraKills']['actual'],
                stats['pentaKills']['actual'],
                "X" if stats['killOrAssistBonus']['actual'] else ""
            ])
    print(tabulate(table2, headers=['Name', 'K', 'D', 'A', 'CS', '3x', '4x', '5x', '10+ K/A']))

    print("")
    print("-"*100)
    print("")