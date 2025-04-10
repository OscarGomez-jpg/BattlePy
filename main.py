from entities.enemy import Enemy
from entities.user import Player
from utils.printer import Printer


def user_ships_placing(user_ships, user_table, totalShips):
    acu = 1
    while acu <= totalShips:
        try:
            print(
                f"Ingrese las coordenadas desde el 1 hasta el {len(user_table)} del barco {acu}: "
            )
            coordX = int(input("Elija la coordenada X: "))
            coordY = int(input("Elija la coordenada Y: "))

            if 0 >= coordX >= len(user_table) or 0 >= coordY >= len(user_table):
                raise ValueError

            coordY -= 1
            coordX -= 1
            acu += 1

            user_ships.append([coordX, coordY])
        except (ValueError, IndexError):
            print(f"Por favor coloca un número del 1 al {len(user_table)}")


def manage_attack(table, attack):
    hitted = table[attack[1]][attack[0]] == "B"

    if hitted:
        table[attack[1]][attack[0]] = "H"
    else:
        table[attack[1]][attack[0]] = "W"


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
            print("!!!Please, only numbers!!!")

    # Creation of both empty maps
    tableToken = "-"
    tablePC = [[tableToken for _ in range(tableSize)] for _ in range(tableSize)]
    tableUser = [[tableToken for _ in range(tableSize)] for _ in range(tableSize)]

    # Game state
    play = True

    pc = Enemy(tablePC, tableUser, totalShips)
    user = Player(tableUser, tablePC, totalShips, userName)
    printer = Printer()

    user_ships_placing(user.ships, user.table, totalShips)

    while play:
        user_coords = user.attack()

        manage_attack(tablePC, user_coords)

        pc_coords = pc.attack()

        manage_attack(tableUser, pc_coords)

        printer.print_table(user.table, user.username, user.ships)
        printer.print_table(pc.table, pc.username, pc.ships)


if __name__ == "__main__":
    main()
