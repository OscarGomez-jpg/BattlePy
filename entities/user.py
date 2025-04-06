from entities.base_entity import Entity


class PlayerBatallaNaval(Entity):
    def __init__(self, table, opponent, totalShips, name) -> None:
        super().__init__(table, opponent, totalShips)
        self.table = table
        self.opponent = opponent
        self.tableSize = len(self.table)
        self.totalShips = totalShips
        self.name = name

    def UserAttack(self):
        attackUserX = int(input("Coordenadas en X del ataque: ")) - 1
        attackUserY = int(input("Coordenadas en Y del ataque: ")) - 1

        # if self.opponentUnseen[attackUserY][attackUserX] == self.ship:
        #     self.opponent[attackUserY][attackUserX] = self.goodHit
        #     self.opponentUnseen[attackUserY][attackUserX] = self.goodHit
        #     self.totalShips -= 1
        # else:
        #     self.opponent[attackUserY][attackUserX] = self.wrongHit
