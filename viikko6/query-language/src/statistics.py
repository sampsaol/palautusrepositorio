from player_reader import PlayerReader
from player import Player


def sort_by_points(player):
    return player.points


class Statistics:
    def __init__(self, player_reader):
        #self._players = player_reader.get_players()
        self._players = [
            Player("Leon Draisaitl", "EDM", 41, 65),
            Player("Connor McDavid", "EDM", 32, 100),
            Player("Garnet Hathaway", "PHI", 7, 10),
            Player("Zach Hyman", "EDM", 54, 23),
            Player("Noah Cates", "PHI", 6, 12),
            Player("Nick Seeler", "PHI", 1, 12),
            Player("Egor Zamula", "PHI", 5, 16),
            Player("Evan Bouchard", "EDM", 18, 64),
            Player("Ryan Nugent-Hopkins", "EDM", 18, 49),
            ]

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top_scorers(self, how_many):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players[:how_many]

    def matches(self, matcher):
        matching_players = filter(
            lambda player: matcher.test(player),
            self._players
        )

        return list(matching_players)
 # type: ignore