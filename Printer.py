class Table():
    def __init__(self, table = [], tableSize = 3) -> None:
        self.table = table
        self.tableSize = tableSize

    def printTable(self):
        for i in range(self.tableSize):
            for j in range(self.tableSize):
                if j < self.tableSize - 1:
                    print(self.table[i][j], end="")
                else:
                    print(self.table[i][j])
    
    def printGame(self, userName, *args):
        for i in args:
            print('----Tablero del PC----')
            self.table = i
            self.printTable()
            print(f'----Tablero de {userName}----')
            self.table = i
            self.printTable()