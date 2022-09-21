class Table():
    def __init__(self, table, tableSize) -> None:
        self.table = table
        self.tableSize = tableSize

    def PrintTable(self):
        for i in range(self.tableSize):
            for j in range(self.tableSize):
                if j < self.tableSize - 1:
                    print(self.table[i][j], end="")
                else:
                    print(self.table[i][j])

    def PrintGame(userName, table1, table2, tableSize):
        print('----Tablero del PC----')
        PrintTable(table2, tableSize)
        print(f'----Tablero de {userName}----')
        PrintTable(table1, tableSize)