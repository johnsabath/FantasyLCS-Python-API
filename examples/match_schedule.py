__author__ = 'John Sabath'

from tabulate import tabulate
from fantasylcs import FantasyLCS

fantasy_lcs = FantasyLCS(season_id=12)
fantasy_lcs.load()


table = []
for match in fantasy_lcs.get_matches():
    row = [
        "Week %d" % match.get_week(),
        match.get_datetime().to('local').format("MMM D, h:mm A"),
        fantasy_lcs.get_team(match.get_blue_team_id()).get_name(),
        fantasy_lcs.get_team(match.get_red_team_id()).get_name(),
        "Y" if match.is_completed() else "N"
    ]
    table.append(row)

print(tabulate(table, headers=["Week", "Date", "Blue Team", "Red Team", "Completed"]))