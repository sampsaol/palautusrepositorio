class TennisGame:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_tied_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_advantage_or_win_score()
        else:
            return self._get_running_score()


    def _get_tied_score(self):
        if self.m_score1 < 3:
            return f"{self.SCORES[self.m_score1]}-All"
        else:
            return "Deuce"
    
    def _get_advantage_or_win_score(self):
        score_difference = self.m_score1 - self.m_score2
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_running_score(self):
        return f"{self.SCORES[self.m_score1]}-{self.SCORES[self.m_score2]}"
