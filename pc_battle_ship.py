from player_battle_ship import Player
import random


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
        self.acu = 0

    def shipsPlacing(self):
        acu = 1
        while acu <= self.total_ships:
            coord_x = random.randint(0, self.table_size - 1)
            coord_y = random.randint(0, self.table_size - 1)

            for ship in self.ships_location:
                if ship[0] != coord_x and ship[0] != coord_y:
                    self.ships_location.append([coord_x, coord_y])
                    acu += 1

    def attack(self, opponent_ships):
        # print(self.acu)
        attack_x = random.randint(0, self.table_size - 1)
        attack_y = random.randint(0, self.table_size - 1)

        if opponent_ships[attack_y][attack_x] == self.ship:
            opponent_ships[attack_y][attack_x] = self.good_hit
            self.total_ships -= 1
        elif opponent_ships[attack_y][attack_x] == self.good_hit:
            self.attack(opponent_ships)
            # self.acu += 1
        elif opponent_ships[attack_y][attack_x] == self.wrong_hit:
            self.attack(opponent_ships)
            # self.acu += 1
        else:
            opponent_ships[attack_y][attack_x] = self.wrong_hit
