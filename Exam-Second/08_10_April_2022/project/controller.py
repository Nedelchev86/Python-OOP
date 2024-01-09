from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player1: Player):
        new_players = []
        for player in player1:
            if player.name not in [p.name for p in self.players]:
                new_players.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(new_players)}"

    def add_supply(self, *supply1: Supply):
        for supply in supply1:
            self.supplies.append(supply)



    def sustain(self, player_name: str, sustenance_type: str):
        if player_name in [p.name for p in self.players]:
            player = [p for p in self.players if p.name == player_name][0]
            if not player._need_sustenance:
                return f"{player_name} have enough stamina."

            if sustenance_type in ["Drink", "Food"]:
                if sustenance_type == "Drink":
                    try:
                        substance = [d for d in self.supplies if d.__class__.__name__ == sustenance_type][-1]
                    except IndexError:
                        raise Exception("There are no drink supplies left!")
                elif sustenance_type == "Food":
                    try:
                        substance = [f for f in self.supplies if f.__class__.__name__ == sustenance_type][-1]
                    except IndexError:
                        raise Exception("There are no food supplies left!")
                if player.stamina + substance.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += substance.energy
                return f"{player_name} sustained successfully with {substance.name}."



    def duel(self, first_player_name: str, second_player_name: str):
        first = [p for p in self.players if p.name == first_player_name][0]
        second = [p for p in self.players if p.name == second_player_name][0]

        if first.stamina == 0 and second.stamina == 0:
            return
        if first.stamina == 0:
            return f"Player {first.name} does not have enough stamina."
        if second.stamina == 0:
            return f"Player {second.name} does not have enough stamina."

        if first.stamina < second.stamina:
            try:
                second.stamina -= first.stamina / 2
            except ValueError:
                second.stamina = 0
            if second.stamina <= 0:
                return f"Winner: {first.name}"
            try:
                first.stamina -= second.stamina / 2
            except ValueError:
                first.stamina = 0
            if first.stamina <= 0:
                return f"Winner: {second.name}"

        if second.stamina < first.stamina:

            try:
                first.stamina -= second.stamina / 2
            except ValueError:
                first.stamina = 0
            if first.stamina <= 0:
                return f"Winner: {second.name}"
            try:
                second.stamina -= first.stamina / 2
            except ValueError:
                second.stamina = 0
            if second.stamina <= 0:
                return f"Winner: {first.name}"

        if first.stamina > second.stamina:
            return f"Winner: {first.name}"
        else:
            return f"Winner: {second.name}"

    def next_day(self):
        pass

    def __str__(self):
        pass