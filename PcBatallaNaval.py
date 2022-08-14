import random


class BatallaNavalIA():
    def __init__(self, tablePC, tablePCUnseen, opponent, totalShips, tableSize=10, wrongHit=' X ', goodHit=' A ', shipToken=' B ') -> None:
        self.tablePC = tablePC
        self.tablePCUnseen = tablePCUnseen
        self.opponent = opponent
        self.totalShips = totalShips
        self.tableSize = tableSize
        self.wrongHit = wrongHit
        self.goodHit = goodHit
        self.ship = shipToken
        self.acu = 0

    def PCShipsPlacing(self):
        acu = 1
        while acu <= self.totalShips:
            coordX = random.randint(0, self.tableSize - 1)
            coordY = random.randint(0, self.tableSize - 1)

            if self.tablePCUnseen[coordY][coordX] != self.ship:
                self.tablePCUnseen[coordY][coordX] = self.ship
                acu += 1

    def Attack(self):
        # print(self.acu)
        attackPCX = random.randint(0, self.tableSize - 1)
        attackPCY = random.randint(0, self.tableSize - 1)

        if self.opponent[attackPCY][attackPCX] == self.ship:
            self.opponent[attackPCY][attackPCX] = self.goodHit
            self.totalShips -= 1
        elif self.opponent[attackPCY][attackPCX] == self.goodHit:
            self.Attack()
            #self.acu += 1
        elif self.opponent[attackPCY][attackPCX] == self.wrongHit:
            self.Attack()
            #self.acu += 1
        else:
            self.opponent[attackPCY][attackPCX] = self.wrongHit
