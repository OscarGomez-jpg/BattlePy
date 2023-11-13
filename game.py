from pc_battle_ship import BatallaNavalIA
from player_battle_ship import Player
from printer import Printer


class Game:
    def __init__(self):
        self.play = True
        self.user_name = ""

    def process_attack(self, source_list, dest_list):
        for coord in dest_list:
            if source_list[0] == coord[0] and source_list[1] == coord[1]:
                dest_list.remove(coord)
                return True
        return False

    def run(self):
        self.user_name = input("Ingrese el nombre de usuario: ")

        # Verifying that the initial inputs are only numbers
        while True:
            try:
                table_size = int(input("Ingrese el tamaño del tablero: "))
                total_ships = int(
                    input("Ingrese la cantidad de barcos con la que jugará: ")
                )
                break
            except ValueError:
                print("!!!Por favor ingrese solo números!!!")

        # Creation the empty map
        table_token_pc = "*"
        table = [[table_token_pc for _ in range(table_size)] for _ in range(table_size)]

        # Characters in the map
        ship = "B"
        wrong_shot = "X"
        good_shot = "A"

        pc = BatallaNavalIA(total_ships, table_size, wrong_shot, good_shot, ship)
        user = Player(total_ships, ship)

        pc.shipsPlacing()

        acu = 0
        while acu < total_ships:
            try:
                print("Ingrese las coordenadas de 1 al 10")
                pos_x = int(input("Ingrese la coodernada X del barco: "))
                pos_y = int(input("Ingrese la coodernada Y del barco: "))
                res = user.shipsPlacing(pos_x, pos_y)
                if res:
                    acu += 1
                else:
                    raise IOError
            except ValueError:
                print("¡Ingrese coordenadas válidas!")
            except IOError:
                print("¡Esa posición ya está ocupada!")

        printer = Printer(table, table_size, self.user_name)
        # printer.printGame(self.user_name)

        while self.play:
            # correct_input = False
            # while not correct_input:
            #     try:
            #         coord_x = int(input("Ingrese la coordenada en x del ataque: "))
            #         coord_y = int(input("Ingrese la coordenada en y del ataque: "))
            #         correct_input = True
            #     except ValueError:
            #         print("¡Ingrese coordenadas válidas!")

            # res = self.process_attack([coord_x, coord_y], pc.ships_location)

            # if res:
            #     printer.table[coord_y][coord_x] = good_shot
            # else:
            #     printer.table[coord_y][coord_x] = wrong_shot

            # pc_coords = pc.attack()
            # pc_res = self.process_attack(pc_coords, user.ships_location)

            # if pc_res:
            #     printer.table[pc_coords[1]][pc_coords[0]] = good_shot
            # else:
            #     printer.table[pc_coords[1]][pc_coords[0]] = wrong_shot

            # printer.printGame(self.user_name)
            printer.printGame()

            # if user.total_ships == 0:
            #     print(f"Ganó {self.user_name}")
            #     self.play = False
            # elif pc.total_ships == 0:
            #     print("Ganó el pc")
            #     self.play = False
