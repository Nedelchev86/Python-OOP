from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {"First": {1: 1_500_000, 2: 800_000}, "Second": {8: 20_000, 10: 10_000}}
        expenses = 250_000
        earned_money = 0

        for key, value in sponsors.items():
            for pos, money in value.items():
                if pos >= race_pos:
                    earned_money += money
                    break
        self.budget += earned_money - expenses

        return f"The revenue after the race is {earned_money - expenses}$. Current budget {self.budget}$"


