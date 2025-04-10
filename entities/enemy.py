from enum import Enum
import random
from typing import Optional, Tuple

from entities.base_entity import Entity


class Region(Enum):
    TOP_LEFT = (0, 0)
    TOP_RIGHT = (1, 0)
    BOTTOM_LEFT = (0, -1)
    BOTTOM_RIGHT = (1, -1)


class LookTable:
    def __init__(self, pos: Tuple[int, int], regions: list[Region]) -> None:
        self.pos = pos
        self.regions = {}

        for region in regions:
            self.regions[region] = False

    def get_pos(self) -> Optional[Tuple[int, int]]:
        filtered_keys = [key for key, value in self.regions.items() if not value]

        if filtered_keys:
            chosen_key: Region = random.choice(filtered_keys)
            self.regions[chosen_key] = True

            to_return = (
                self.pos[0] + chosen_key.value[0],
                self.pos[1] + chosen_key.value[1],
            )

            return to_return

        return None


class Enemy(Entity):
    def __init__(self, table, opponent_table, total_ships, username="PC") -> None:
        super().__init__(table, opponent_table, total_ships, username=username)
        self.acu = 0
        self.table_size = len(self.table)
        self.ships = []

        # This means that the enemy will look in a 2x2 matrix
        self.look_table_size = 2
        self.look_tables: list[LookTable] = []

        self.generate_attacks()

        # A follow of the look tables to throw the dices
        self.non_visited_look_tables = set(range(len(self.look_tables)))

    def ships_placing(self):
        acu = 1
        while acu <= self.total_ships:
            coordX = random.randint(0, self.table_size - 1)
            coordY = random.randint(0, self.table_size - 1)

            if self.table[coordY][coordX] not in self.ships:
                self.table[coordY][coordX] = self.ship_token
                acu += 1

    def generate_attacks(self):
        for i in range(0, len(self.table), self.look_table_size):
            for j in range(0, len(self.table[0]), self.look_table_size):
                # Represents X, Y, isVisited
                self.look_tables.append(
                    LookTable(
                        (j, i),
                        [
                            Region.TOP_LEFT,
                            Region.TOP_RIGHT,
                            Region.BOTTOM_LEFT,
                            Region.BOTTOM_RIGHT,
                        ],
                    )
                )

    def clamp(self, pos: int) -> int:
        return min(pos, self.table_size)

    def attack(self) -> list[int]:
        pos_x = -1
        pos_y = -1
        valid_look_table = False

        while not valid_look_table:
            new_index = random.choice(list(self.non_visited_look_tables))

            # look table choosen
            new_look_table = self.look_tables[new_index]
            pos = new_look_table.get_pos()

            if pos is not None:
                pos_x, pos_y = pos
                pos_x = self.clamp(pos_x)
                pos_y = self.clamp(pos_y)
                valid_look_table = True
            else:
                self.non_visited_look_tables.remove(new_index)

        return [pos_x, pos_y]
