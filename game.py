from pc_battle_ship import BatallaNavalIA
from player_battle_ship import Player
from printer import Printer


class Game:
    def __init__(self):
        self.play = True
        self.user_name = ""

    def process_attack(self, source, dest):
        pass

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

        # Creation of both empty maps
        table_token_pc = " * "
        table_token_user = " - "
        table = [[table_token_pc for _ in range(table_size)] for _ in range(table_size)]

        # Some values to assign an character in the game
        ship = " B "
        wrong_shot = " X "
        good_shot = " A "

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

        pt = Printer(table_size)
        pt.printGame(self.user_name, table)

        while self.play:
            pc.attack(user.ships_location)
            pt.printGame(self.user_name, table)

            if user.total_ships == 0:
                print(f"Ganó {self.user_name}")
                self.play = False
            elif pc.total_ships == 0:
                print("Ganó el pc")
                self.play = False
