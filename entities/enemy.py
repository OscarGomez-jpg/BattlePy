import random

from entities.base_entity import Entity


class Enemy(Entity):
    def __init__(
        self,
        table,
        opponent_table,
        total_ships,
    ) -> None:
        super().__init__(table, opponent_table, total_ships)
        self.acu = 0
        self.table_size = len(self.table)
        self.ships = []

    def ships_placing(self):
        acu = 1
        while acu <= self.total_ships:
            coordX = random.randint(0, self.table_size - 1)
            coordY = random.randint(0, self.table_size - 1)

            if self.table[coordY][coordX] not in self.ships:
                self.table[coordY][coordX] = self.ship_token
                acu += 1

    # TODO: Add a real track, simple look for more parts in bigger ships
    def Attack(self):
        # print(self.acu)
        attackPCX = random.randint(0, self.table_size - 1)
        attackPCY = random.randint(0, self.table_size - 1)

        if self.opponent_table[attackPCY][attackPCX] == self.ship_token:
            self.opponent_table[attackPCY][attackPCX] = self.good_hit_symbol
            self.total_ships -= 1
        elif self.opponent_table[attackPCY][attackPCX] == self.good_hit_symbol:
            self.Attack()
            # self.acu += 1
        elif self.opponent_table[attackPCY][attackPCX] == self.wrong_hit_symbol:
            self.Attack()
            # self.acu += 1
        else:
            self.opponent_table[attackPCY][attackPCX] = self.wrong_hit_symbol
