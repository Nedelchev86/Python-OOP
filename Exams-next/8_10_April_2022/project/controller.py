class Controller:
    VALID_SUBSTANCE = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        new_players = [p for p in args if p not in self.players]
        self.players.extend(new_players)
        return f"Successfully added: {', '.join([p.name for p in new_players])}"

    def add_supply(self, *args):
        [self.supplies.append(s) for s in args]

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return

        if sustenance_type not in self.VALID_SUBSTANCE:
            return

        try:
            food = [d for d in reversed(self.supplies) if d.__class__.__name__ == sustenance_type][0]
        except Exception:
            raise Exception("There are no food supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if player.stamina + food.energy > 100:
            player.stamina = 100
        else:
            player.stamina += food.energy

        for i in range(len(self.supplies) -1, 0, -1):
            if self.supplies[i] == food:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {food.name}."

    # def duel(self, first_player_name: str, second_player_name: str):
    #     player1 = [p for p in self.players if p.name == first_player_name][0]
    #     player2 = [p for p in self.players if p.name == second_player_name][0]
    #
    #     if player1.stamina == 0 and player2.stamina == 0:
    #         return f"Player {player1.name} does not have enough stamina.\nPlayer {player2.name} does not have enough stamina."
    #     if player1.stamina == 0:
    #         return f"Player {player1.name} does not have enough stamina."
    #     if player2.stamina == 0:
    #         return f"Player {player2.name} does not have enough stamina."
    #
    #     if player1.stamina < player2.stamina:
    #         player2.stamina -= player1.stamina / 2
    #         if player2.stamina <= 0:
    #             player2.stamina = 0
    #             return f"Winner: {player1.name}"
    #         player1.stamina -= player2.stamina / 2
    #         if player1.stamina <= 0:
    #             player1.stamina = 0
    #             return f"Winner: {player2.name}"
    #
    #     else:
    #         player1.stamina -= player2.stamina / 2
    #         if player1.stamina <= 0:
    #             player1.stamina = 0
    #             return f"Winner: {player2.name}"
    #         player2.stamina -= player1.stamina / 2
    #         if player2.stamina <= 0:
    #             player2.stamina = 0
    #             return f"Winner: {player1.name}"
    #
    #     if player2.stamina < player1.stamina:
    #         return f"Winner: {player1.name}"
    #     else:
    #         return f"Winner: {player2.name}"


    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\nPlayer {second_player.name} does not have enough stamina."
        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)



    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        [result.append(str(p)) for p in self.players]
        [result.append(s.details()) for s in self.supplies]
        return "\n".join(result)