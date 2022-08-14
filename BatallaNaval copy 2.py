

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
tablePC = [[tableTokenPC for _ in range(tableSize)] for _ in range(tableSize)]
tablePCUnseen = [[tableTokenPC for _ in range(tableSize)] for _ in range(tableSize)]
tableUser = [[tableTokenUser for _ in range(tableSize)] for _ in range(tableSize)]

# Some values to assign an image in the game
ship = ' B '
wrongShot = ' X '
goodShot = ' A '
play = True
shipsUser = totalShips
shipsPC = totalShips


def PrintTable(table, tableSize):
    for i in range(tableSize):
        for j in range(tableSize):
            if j < tableSize - 1:
                print(table[i][j], end="")
            else:
                print(table[i][j])


def PrintGame(userName, table1, table2, tableSize):
    print('----Tablero del PC----')
    PrintTable(table2, tableSize)
    print(f'----Tablero de {userName}----')
    PrintTable(table1, tableSize)

# Verifying that the user doesn't introduce a wrong coord
# Implements the total of ships to the user


PrintGame(userName, tableUser, tablePC, tableSize)

while play:
    

    PrintGame(userName, tableUser, tablePC, tableSize)

    if shipsPC == 0:
        print(f"Ganó {userName}")
        play = False
    elif shipsUser == 0:
        print("Ganó el pc")
        play = False
