class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        top_scorers = []
        for player in players:
            if player.nationality == nationality:
                top_scorers.append(player)

        sorted_players = sorted(top_scorers, key=lambda player: player.goals + player.assists, reverse=True)
        return sorted_players
