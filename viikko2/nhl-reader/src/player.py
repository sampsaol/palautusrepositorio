class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']

    
    def __str__(self):
        player = f"{self.name:20} {self.team} goals {self.goals} assists {self.assists}"
        return player
