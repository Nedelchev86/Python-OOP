from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {"First": {1: 1500000, 2: 800000}, "Second": {8: 20000, 10: 10000}}
        expenses = 250000
        earned_money = 0

        for key, value in sponsors.items():
            for pos, money in value.items():
                if race_pos <= pos:
                    earned_money += money
                    break
        result = earned_money - expenses
        self.budget += result
        return f"The revenue after the race is {result}$. Current budget {self.budget}$"
