from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {"First": {1: 1_000_000, 2: 500_000}, "Second": {5: 100_000, 7: 50_000}}
        earned_money = 0
        expenses = 200_000

        for key, value in sponsors.items():
            for pos, money in value.items():
                if pos >= race_pos:
                    earned_money += money
                    break
        self.budget += earned_money - expenses

        return f"The revenue after the race is {earned_money - expenses}$. Current budget {self.budget}$"






