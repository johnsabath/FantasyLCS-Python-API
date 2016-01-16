__author__ = 'John Sabath'

import arrow
import requests

ALL_PLAYER_STAT_NAMES = ["matchesPlayed", "kills", "deaths", "assists", "minionKills", "doubleKills", "tripleKills", "quadraKills", "pentaKills", "killOrAssistBonus"]
ALL_TEAM_STAT_NAMES = ["matchesPlayed", "firstBlood", "towerKills", "baronKills", "dragonKills", "matchVictory", "matchDefeat", "secondsPlayed", "quickWinBonus"]
ALL_TREND_STAT_NAMES = ["ownerPercentage", "startingPercentage", "startingCount", "totalAdds", "totalDrops"]
ALL_ROSTER_POSITIONS = ["TOP_LANE", "JUNGLER", "MID_LANE", "AD_CARRY", "SUPPORT"]


def _parse_trends(data):
    return dict(zip(ALL_TREND_STAT_NAMES, data))


class FantasyLCS(object):
    data = {}
    season_id = None

    teams = {}
    players = {}
    matches = {}

    def __init__(self, season_id):
        self.season_id = season_id

    def load(self):
        self.data = requests.get("http://fantasy.na.lolesports.com/en-US/api/season/%d" % self.season_id).json()

        for team in self.data['proTeams']:
            self.teams[team['id']] = Team(team, self)

        for match in self.data['proMatches']:
            self.matches[match['id']] = Match(match, self)

        for player in self.data['proPlayers']:
            self.players[player['id']] = Player(player, self)

    def get_season_name(self):
        return self.data['seasonName']

    def get_split(self):
        return self.data['seasonSplit']

    def get_begin_datetime(self):
        return arrow.get(*self.data['seasonBegins'], tzinfo="US/Pacific")

    def get_end_datetime(self):
        return arrow.get(*self.data['seasonEnds'], tzinfo="US/Pacific")

    def get_num_weeks(self):
        return self.data['numberOfWeeks']

    def get_bye_weeks(self):
        return self.data['byeWeeks']

    def get_weekly_roster_locks(self):
        out = []
        for week in self.data['rosterLocksByWeek']:
            week_data = {}
            for region in self.data['rosterLocksByWeek'][week]:
                week_data[region] = arrow.get(*self.data['rosterLocksByWeek'][week][region])
            out.append(week_data)
        return out

    def get_teams(self):
        return self.teams.values()

    def get_matches(self):
        return sorted(self.matches.values(), key=lambda x: x.get_datetime())

    def get_players(self):
        return self.players.values()

    def get_player(self, _id):
        return self.players.get(_id)

    def get_team(self, _id):
        return self.teams.get(_id)

    def get_match(self, _id):
        return self.matches.get(_id)


class Player(object):
    data = {}
    _fantasylcs = None

    def __init__(self, player_data, fantasylcs):
        self.data = player_data
        self._fantasylcs = fantasylcs

    def get_id(self):
        return self.data['id']

    def get_riot_id(self):
        return self.data['riotId']

    def get_name(self):
        return self.data['name']

    def get_photo_url(self):
        return self.data['photoUrl']

    def get_positions(self):
        return self.data['positions']

    def get_team_id(self):
        return self.data['proTeamId']

    @staticmethod
    def _parse_player_stats(data):
        i = 0
        out = {}

        for key in ALL_PLAYER_STAT_NAMES:
            out[key] = {
                'projected': data[i],
                'actual': data[i+1]
            }
            i += 2

        return out

    def get_season_stats(self):
        return Player._parse_player_stats(self.data['statsBySeason'])

    def get_weekly_stats(self):
        return [Player._parse_player_stats(self.data['statsByWeek'][week]) for week in self.data['statsByWeek']]

    def get_match_stats(self):
        out = {}
        for match_id in self.data['statsByMatch']:
            out[match_id] = Player._parse_player_stats(self.data['statsByMatch'][match_id])
        return out

    def get_weekly_trends(self):
        return [_parse_trends(self.data['trendsByWeek'][a]) for a in self.data['trendsByWeek']]


class Match(object):
    data = {}
    _fantasylcs = None

    def __init__(self, match_data, fantasylcs):
        self.data = match_data
        self._fantasylcs = fantasylcs

    def get_id(self):
        return self.data['id']

    def get_riot_id(self):
        return self.data['riotId']

    def get_week(self):
        return self.data['week']

    def get_datetime(self):
        return arrow.get(*self.data['time'], tzinfo="US/Pacific")

    def get_red_team_id(self):
        return self.data['redTeamId']

    def get_blue_team_id(self):
        return self.data['blueTeamId']

    def is_completed(self):
        return self.data['complete']


class Team(object):
    data = {}
    _fantasylcs = None

    def __init__(self, team_data, fantasylcs):
        self.data = team_data
        self._fantasylcs = fantasylcs

    def get_id(self):
        return self.data['id']

    def get_riot_id(self):
        return self.data['riotId']

    def get_name(self):
        return self.data['name']

    def get_acronym(self):
        return self.data['shortName']

    def get_logo_url(self):
        return self.data['logoUrl']

    def get_league(self):
        return self.data['league']

    @staticmethod
    def _parse_team_stats(data):
        i = 0
        out = {}

        for key in ALL_TEAM_STAT_NAMES:
            out[key] = {
                'projected': data[i],
                'actual': data[i+1]
            }
            i += 2

        return out

    def get_season_stats(self):
        return Team._parse_team_stats(self.data['statsBySeason'])

    def get_weekly_stats(self):
        return [Team._parse_team_stats(self.data['statsByWeek'][week]) for week in self.data['statsByWeek']]

    def get_match_stats(self):
        out = {}
        for match_id in self.data['statsByMatch']:
            out[match_id] = Team._parse_team_stats(self.data['statsByMatch'][match_id])
        return out

    def get_weekly_trends(self):
        return [_parse_trends(self.data['trendsByWeek'][a]) for a in self.data['trendsByWeek']]

