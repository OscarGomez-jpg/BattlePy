import random
from player_battle_ship import Player


class BatallaNavalIA(Player):
    def __init__(
        self,
        total_ships,
        table_size,
        wrong_hit=" X ",
        good_hit=" A ",
        ship_token=" B ",
    ) -> None:
        super().__init__(total_ships, ship_token)
        self.total_ships = total_ships
        self.table_size = table_size
        self.wrong_hit = wrong_hit
        self.good_hit = good_hit
        self.ship = ship_token

    def shipsPlacing(self):
        acu = 0
        while acu < self.total_ships:
            coord_x = random.randint(0, self.table_size - 1)
            coord_y = random.randint(0, self.table_size - 1)

            add = True
            for ship_l in self.ships_location:
                if ship_l[0] == coord_x and ship_l[1] == coord_y:
                    add = False

            if add:
                self.ships_location.append([coord_x, coord_y])
                acu += 1

    def attack(self):
        # print(self.acu)
        attack_x = random.randint(0, self.table_size - 1)
        attack_y = random.randint(0, self.table_size - 1)

        return [attack_x, attack_y]
