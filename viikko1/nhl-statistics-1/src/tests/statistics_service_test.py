import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_searching_existing_player(self):
        player = self.stats.search("Semenko")

        self.assertAlmostEqual(player.name, "Semenko")

    def test_searching_nonexisting_player(self):
        player = self.stats.search("Nobody")

        self.assertAlmostEqual(player, None)

    def test_team_search_works(self):
        team = self.stats.team("EDM")

        self.assertEqual(len(team), 3)

        names = []
        for player in team:
            names.append(player.name)

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_scorers_fetches_right_amount(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(len(players), 3)

    def test_top_scorers_fethces_right_players(self):
        players = self.stats.top(3,SortBy.POINTS)

        names = []
        for player in players:
            names.append(player.name)

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_assisters_works(self):
        players = self.stats.top(3,SortBy.ASSISTS)
        self.assertEqual(len(players), 3)

        names = []
        for player in players:
            names.append(player.name)

        self.assertEqual(names, ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_goals_works(self):
        players = self.stats.top(3,SortBy.GOALS)
        self.assertEqual(len(players), 3)

        names = []
        for player in players:
            names.append(player.name)

        self.assertEqual(names, ["Lemieux", "Yzerman", "Kurri"])
        