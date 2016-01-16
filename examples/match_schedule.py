__author__ = 'John Sabath'

from tabulate import tabulate
from fantasylcs import FantasyLCS

fantasy_lcs = FantasyLCS(season_id=12)
fantasy_lcs.load()

# Index the teams first
teams = {}
for team in fantasy_lcs.get_teams():
    teams[team.get_id()] = team

# Then build the table
table = []
for match in fantasy_lcs.get_matches():
    row = [
        "Week %d" % match.get_week(),
        match.get_datetime().to('local').format("MMM D, h:mm A"),
        teams[match.get_blue_team_id()].get_name(),
        teams[match.get_red_team_id()].get_name(),
        "Y" if match.is_completed() else "N"
    ]
    table.append(row)

print(tabulate(table, headers=["Week", "Date", "Blue Team", "Red Team", "Completed"]))