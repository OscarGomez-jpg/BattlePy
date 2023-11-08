class Printer:
    def __init__(self, table, table_size=3) -> None:
        self.table = table
        self.table_size = table_size

    def printTable(self):
        for i in range(self.table_size):
            for j in range(self.table_size):
                print(self.table[i][j], end="")
            print(self.table[i][j])

    def printGame(self, user_name, *args):
        for i in args:
            print("----Tablero del PC----")
            self.table = i
            self.printTable()
            print(f"----Tablero de {user_name}----")
            self.table = i
            self.printTable()
