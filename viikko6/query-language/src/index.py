from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    #reader = PlayerReader(url)
    reader = [
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
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = query.plays_in("EDM").has_at_least(10, "goals").has_fewer_than(50, "goals").build()
    print()
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
