from entities.base_entity import Entity


class Player(Entity):
    def __init__(self, table, opponent, total_ships, username) -> None:
        super().__init__(
            table=table,
            opponent_table=opponent,
            total_ships=total_ships,
            username=username,
        )

    def attack(self) -> list[int]:
        pos = ""
        pos_x = 0
        pos_y = 0
        confirmed = False

        while not confirmed:
            try:
                pos = input(f"Coordinates (1 to {len(self.table)}): ")
                pos = pos.split(" ")

                if len(pos) != 2:
                    raise ValueError

                pos_x = int(pos[0]) - 1
                pos_y = int(pos[1]) - 1

                confirmed = True
            except ValueError:
                print("Give the coordinates separated by a space: X Y")

        return [pos_x, pos_y]
