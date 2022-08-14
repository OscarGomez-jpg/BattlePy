from BatallaNaval import PrintTable as pt


class PlayerBatallaNaval():
    def __init__(self, table, opponent, opponentUnseen, tableSize, totalShips, shipToken, userName, wrongHit, goodHit) -> None:
        self.table = table
        self.opponent = opponent
        self.opponentUnseen = opponentUnseen
        self.tableSize = tableSize
        self.totalShips = totalShips
        self.ship = shipToken
        self.name = userName
        self.wrongHit = wrongHit
        self.goodHit = goodHit

    def UserShipsPlacing(self):
        acu = 1
        while acu <= self.totalShips:
            try:
                print(
                    f"Ingrese las coordenadas desde el 1 hasta el {self.tableSize} del barco {acu}: ")
                coordX = int(input("Elija la coordenada X: "))
                coordY = int(input("Elija la coordenada Y: "))

                if coordX == 0 or coordY == 0:
                    raise ValueError

                coordY -= 1
                coordX -= 1
                self.table[coordY][coordX] = self.ship
                pt(self.table, self.tableSize)
                acu += 1
            except (ValueError, IndexError):
                print(f"Por favor coloca un número del 1 al {self.tableSize}")

    def UserAttack(self):
        attackUserX = int(input("Coordenadas en X del ataque: ")) - 1
        attackUserY = int(input("Coordenadas en Y del ataque: ")) - 1

        if self.opponentUnseen[attackUserY][attackUserX] == self.ship:
            self.opponent[attackUserY][attackUserX] = self.goodHit
            self.opponentUnseen[attackUserY][attackUserX] = self.goodHit
            self.totalShips -= 1
        else:
            self.opponent[attackUserY][attackUserX] = self.wrongHit
