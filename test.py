from PcBatallaNaval import BatallaNavalIA
from UserBatallaNaval import PlayerBatallaNaval

tableSize = 10
totalShips = 20
tableTokenPC = ' * '
ship = ' B '
tablePC = [[tableTokenPC for _ in range(tableSize)] for _ in range(tableSize)]
acu2 = 0
acu3 = 0
acu4 = 0

#pc = BatallaNavalIA(tablePC, tablePC, tablePC, totalShips, tableSize)
user = PlayerBatallaNaval(tablePC, tablePC, tablePC, tableSize, totalShips, ship, "Oscar", ' X ', ' A ')

#pc.PCShipsPlacing()
user.UserShipsPlacing()

#for i in range(20):
#    pc.Attack()

for i in range(tableSize):
    for j in range(tableSize):
        if j == 9:
            print(tablePC[i][j])
            if tablePC[i][j] == ' B ':
                acu2 += 1
            elif tablePC[i][j] == ' X ':
                acu3 += 1
            elif tablePC[i][j] == ' A ':
                acu4 += 1
        else:
            print(tablePC[i][j], end="")
            if tablePC[i][j] == ' B ':
                acu2 += 1
            elif tablePC[i][j] == ' X ':
                acu3 += 1
            elif tablePC[i][j] == ' A ':
                acu4 += 1

#print("Total de barcos: ", acu2)
print("Total de disparos errados: ", acu3)
print("Total de disparos acertados: ", acu4)

#print(tablePC[2])
#print(tablePC[3])
