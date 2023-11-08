class Player:
    def __init__(self, total_ships, ship_token) -> None:
        self.total_ships = total_ships
        self.ship_token = ship_token
        self.ships_location = []

    def shipsPlacing(self, pos_x, pos_y) -> bool:
        for ship in self.ships_location:
            if pos_x != ship[0] and pos_y != ship[1]:
                self.ships_location.append([pos_x, pos_y])
                return True
        return False
