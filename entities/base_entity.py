class Entity:
    def __init__(
        self,
        table: list,
        opponent_table: list,
        total_ships: int,
        wrong_hit_symbol="X",
        good_hit_symbol="A",
        ship_token="B",
        ships: list = [],
    ) -> None:
        self.table = table
        self.opponent_table = opponent_table
        self.total_ships = total_ships
        self.wrong_hit_symbol = wrong_hit_symbol
        self.good_hit_symbol = good_hit_symbol
        self.ship_token = ship_token
        self.ships = ships

    def ships_placing(self):
        pass

    def attack(self):
        pass
