from Printer import Table
from entities.enemy import Enemy
from entities.user import PlayerBatallaNaval


def user_ships_placing(user_table, totalShips):
    acu = 1
    while acu <= totalShips:
        try:
            print(
                f"Ingrese las coordenadas desde el 1 hasta el {len(user_table)} del barco {acu}: "
            )
            coordX = int(input("Elija la coordenada X: "))
            coordY = int(input("Elija la coordenada Y: "))

            if coordX == 0 or coordY == 0:
                raise ValueError

            coordY -= 1
            coordX -= 1
            acu += 1
        except (ValueError, IndexError):
            print(f"Por favor coloca un número del 1 al {len(user_table)}")


def main():
    userName = input("Insert username: ")
    verified = False
    tableSize = 0
    totalShips = 0

    # Verifying that the initial inputs are only numbers
    while not verified:
        try:
            tableSize = int(input("Insert table size: "))
            totalShips = int(input("Insert total ships: "))
            verified = True
        except ValueError:
            print("!!!Por favor ingrese solo números!!!")

    # Creation of both empty maps
    tableToken = " - "
    tablePC = [[tableToken for _ in range(tableSize)] for _ in range(tableSize)]
    tablePCUnseen = [[tableToken for _ in range(tableSize)] for _ in range(tableSize)]
    tableUser = [[tableToken for _ in range(tableSize)] for _ in range(tableSize)]

    user_ships_placing(tableUser, totalShips)

    # Some values to assign an image in the game
    ship = " B "
    wrongShot = " X "
    goodShot = " A "
    play = True

    pc = Enemy(tablePC, tableUser, totalShips)

    user = PlayerBatallaNaval(tableUser, tablePC, totalShips, userName)

    pt = Table(tableSize)

    pt.printGame(userName, tablePC, tableUser)

    while play:
        user.UserAttack()

        pc.Attack()

        # PrintGame(userName, tableUser, tablePC, tableSize)

        # TODO Recordar cambiar lo de total ships, para que cada clase maneje su propio contador de barcos
        # if user.totalShips == 0:
        #     print(f"Ganó {userName}")
        #     play = False
        # elif pc.totalShips == 0:
        #     print("Ganó el pc")
        #     play = False


if __name__ == "__main__":
    main()
