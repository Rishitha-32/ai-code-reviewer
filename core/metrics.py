class Metrics:

    def calculate_score(self, issues):
        score = 100 - (len(issues) * 10)
        return max(score, 0)
