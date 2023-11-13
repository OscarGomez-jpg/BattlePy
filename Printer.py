from time import sleep
from asciimatics.screen import ManagedScreen


class Printer:
    def __init__(self, table, table_size=3, user_name="Player") -> None:
        self.table = table
        self.table_pos_y = 10
        self.table_pos_x = 0
        self.table_size = table_size
        self.user_name = user_name

    def printGame(self):
        with ManagedScreen() as screen:
            screen.print_at("---Tablero del PC---", int(screen.width / 2 - 10), 5)

            for i in range(self.table_size):
                for j in range(self.table_size * 2):
                    screen.print_at(
                        self.table[i][j], self.table_pos_x + j, self.table_pos_y
                    )
                self.table_pos_y += 1

            self.table_pos_y = 10
            screen.refresh()
            sleep(0.5)
