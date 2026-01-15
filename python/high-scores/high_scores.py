class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)
    
    def personal_top_three(self):
        top_three = (sorted(self.scores))
        top_three.reverse()
        return top_three[:3]
