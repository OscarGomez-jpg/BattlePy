from PcBatallaNaval import BatallaNavalIA
from UserBatallaNaval import PlayerBatallaNaval
from Printer import Table


def main():
    print("Ingrese el nombre de usuario: ")
    userName = input()

    # Verifying that the initial inputs are only numbers
    while True:
        try:
            print("Ingrese el tamaño del tablero: ")
            tableSize = int(input())
            print("Ingrese la cantidad de barcos con la que jugará: ")
            totalShips = int(input())
            break
        except ValueError:
            print("!!!Por favor ingrese solo números!!!")

    # Creation of both empty maps
    tableTokenPC = ' * '
    tableTokenUser = ' - '
    tablePC = [[tableTokenPC for _ in range(
        tableSize)] for _ in range(tableSize)]
    tablePCUnseen = [[tableTokenPC for _ in range(
        tableSize)] for _ in range(tableSize)]
    tableUser = [[tableTokenUser for _ in range(
        tableSize)] for _ in range(tableSize)]

    # Some values to assign an image in the game
    ship = ' B '
    wrongShot = ' X '
    goodShot = ' A '
    play = True
    shipsUser = totalShips
    shipsPC = totalShips

    pc = BatallaNavalIA(tablePC, tablePCUnseen, tableUser,
                        totalShips, tableSize, wrongShot, goodShot, ship)

    user = PlayerBatallaNaval(tableUser, tablePC, tablePCUnseen,
                              tableSize, totalShips, ship, userName, wrongShot, goodShot)

    pc.PCShipsPlacing()

    user.UserShipsPlacing()

    pt = Table(tableSize)

    pt.printGame(userName, tablePC, tableUser)

    while play:
        user.UserAttack()

        pc.Attack()

        PrintGame(userName, tableUser, tablePC, tableSize)

        # TODO Recordar cambiar lo de total ships, para que cada clase maneje su propio contador de barcos
        if user.totalShips == 0:
            print(f"Ganó {userName}")
            play = False
        elif pc.totalShips == 0:
            print("Ganó el pc")
            play = False


if __name__ == "__main__":
    main()
