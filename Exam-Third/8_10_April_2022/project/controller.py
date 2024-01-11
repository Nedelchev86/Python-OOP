from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player.name in [p.name for p in  self.players]:
                continue
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [p.name for p in self.players]:
            return

        if sustenance_type not in ["Food", "Drink"]:
            return

        try:
            substance = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
        except IndexError:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player = [p for p in self.players if p.name == player_name][0]

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if player.stamina + substance.energy > 100:
            player.stamina = 100
        else:
            player.stamina += substance.energy

        for s in range(len(self.supplies) -1, -1, -1):
            if self.supplies[s].__class__.__name__ == sustenance_type:
                self.supplies.pop(s)
                break

        return f"{player_name} sustained successfully with {substance.name}."


    def duel(self, first_player_name: str, second_player_name: str):
        player1 = [p for p in self.players if p.name == first_player_name][0]
        player2 = [p for p in self.players if p.name == second_player_name][0]

        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\nPlayer {player2.name} does not have enough stamina."
        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        if player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."

        if player1.stamina < player2.stamina:
            if player2.stamina - (player1.stamina /2) <= 0:
                player2.stamina = 0
                return f"Winner: {player1.name}"
            else:
                player2.stamina -= (player1.stamina / 2)

            if player1.stamina - (player2.stamina /2) <= 0:
                player1.stamina = 0
                return f"Winner: {player2.name}"
            else:
                player1.stamina -= (player2.stamina / 2)

        if player2.stamina < player1.stamina:
            if player1.stamina - (player2.stamina / 2) <= 0:
                player1.stamina = 0
                return f"Winner: {player2.name}"
            else:
                player1.stamina -= (player2.stamina / 2)

            if player2.stamina - (player1.stamina / 2) <= 0:
                player2.stamina = 0
                return f"Winner: {player1.name}"
            else:
                player2.stamina -= (player1.stamina / 2)

        if player1.stamina > player2.stamina:
            return f"Winner: {player1.name}"
        else:
            return f"Winner: {player2.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (2 * player.age) < 0:
                player.stamina = 0
            else:
                player.stamina -= ( player.age * 2)

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")


    def __str__(self):
        result = []
        [result.append(str(p)) for p in self.players]
        [result.append(s.details()) for s in self.supplies]
        return "\n".join(result)
