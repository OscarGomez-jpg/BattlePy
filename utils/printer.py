class Printer:
    def __init__(self) -> None:
        self.separator = " "

    def print_table(self, table, username, ships):
        print(f"{username} table")
        for i in range(len(table)):
            for j in range(len(table[0])):
                print(self.separator, table[i][j], end=" ")
            print()
