from game_board import Board, OutOfBoundariesException, \
    AlreadyUsedException
from ships import Dot
from random import randint

BOARD_SIZE = 6
SHIPS = [3, 2, 2, 1, 1, 1, 1]


class Game:
    """Main class for the game"""
    def __init__(self, player_b, computer_b):
        self.game_on = True
        self.player_board = player_b
        self.computer_board = computer_b

    def game_boards(self):
        """Printing both boards"""
        print("User board:")
        self.player_board.print_board()
        print("Computer board:")
        self.computer_board.print_board()

    def player_turn(self):
        """Player turn logic"""
        print("Player turn:")
        while True:
            answer = input("Type coordinates 0 to 5 as: x y: ").split()
            if len(answer) != 2:
                print("Enter coordinates 0 to 5 as: x y: ")
                continue
            try:
                x = int(answer[0])
                y = int(answer[1])
            except ValueError:
                print("Coordinates must be integers")
                continue

            try:
                return True if computer_board.strike(Dot(x, y), True) else False

            except OutOfBoundariesException as e:
                print(e)
            except AlreadyUsedException as e:
                print(e)

    def computer_turn(self):
        """Computer turn logic"""
        dot = Dot(randint(0, 5), randint(0, 5))
        # print(f"Computer turn: {dot}")

        try:
            return False if player_board.strike(dot, False) else True

        except OutOfBoundariesException as e:
            print(e)
        except AlreadyUsedException as e:
            print(e)

    def start_game(self):
        """Game start method"""
        player = True
        print("**********************")
        print("***   Battleship   ***")
        print("**********************")
        print()
        self.game_boards()
        while self.game_on:

            if player:
                player = self.player_turn()
            else:
                player = self.computer_turn()

            if self.computer_board.counter == 7:
                print("Player WON!")
                self.game_on = False

            if self.player_board.counter == 7:
                print("Computer WON!")
                self.game_on = False

            print(f"computer {self.computer_board.counter}")
            print(f"player {self.player_board.counter}")
            self.game_boards()


player_board = Board(BOARD_SIZE)
computer_board = Board(BOARD_SIZE)
player_board.place_ships(SHIPS, BOARD_SIZE, computer=False)
computer_board.place_ships(SHIPS, BOARD_SIZE, computer=True)

game = Game(player_board, computer_board)

if __name__ == '__main__':
    game.start_game()
