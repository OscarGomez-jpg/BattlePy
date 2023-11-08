from pc_battle_ship import BatallaNavalIA
from player_battle_ship import Player
from printer import Table


def main():
    """
    Main game loop for the Battleship game.

    The game starts by prompting the user to enter their name and the size of the game board.
    The user is then prompted to enter the number of ships they will use.

    The game then creates two empty maps, one for the player and one for the computer.
    Each map is filled with asterisks ('*') to represent the squares on the game board.

    The game then assigns an image to each ship, and sets the initial state of the game.
    The player and computer take turns placing their ships on the game board.

    The game ends when one player's ships are all sunk or when both players have placed all of
    their ships.
    The winner is determined by the number of ships remaining on the game board.

    The game uses the `BatallaNavalIA` class to represent the computer's moves, and the
    `PlayerBatallaNaval` class to represent the player's moves. The `Table` class is used to
    print the game board and keep track of the game state.

    The game uses a `while` loop to continue playing until the game is over.
    The loop checks if either player has won, and if not, it continues to the next turn.

    The game also includes some comments to explain the purpose of each part of the code.
    """
    print("Ingrese el nombre de usuario: ")
    user_name = input()

    # Verifying that the initial inputs are only numbers
    while True:
        try:
            print("Ingrese el tamaño del tablero: ")
            table_size = int(input())
            print("Ingrese la cantidad de barcos con la que jugará: ")
            total_ships = int(input())
            break
        except ValueError:
            print("!!!Por favor ingrese solo números!!!")

    # Creation of both empty maps
    table_token_pc = " * "
    table_token_user = " - "
    table_pc = [[table_token_pc for _ in range(table_size)] for _ in range(table_size)]
    table_user = [
        [table_token_user for _ in range(table_size)] for _ in range(table_size)
    ]

    # Some values to assign an image in the game
    ship = " B "
    wrong_shot = " X "
    good_shot = " A "
    play = True

    pc = BatallaNavalIA(total_ships, table_size, wrong_shot, good_shot, ship)
    user = Player(total_ships, ship)

    pc.shipsPlacing()

    user.shipsPlacing(0, 0)

    pt = Table(table_size)

    pt.printGame(user_name, table_pc, table_user)

    while play:
        pc.attack(user.ships_location)

        pt.printGame(user_name, table_user, table_pc, table_size)

        if user.total_ships == 0:
            print(f"Ganó {user_name}")
            play = False
        elif pc.total_ships == 0:
            print("Ganó el pc")
            play = False


if __name__ == "__main__":
    main()
