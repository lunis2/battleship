from random import randint

from ships import Dot, Ship

SEA = "~"
FIRE = "X"
HIT = "*"


class OutOfBoundariesException(BaseException):
    def __str__(self):
        return "Out of boundaries"


class AlreadyUsedException(BaseException):
    def __str__(self):
        return "These coordinates were used previously"


class ShipPositioningException(BaseException):
    def __str__(self):
        return "Couldn't position the ship"


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.ships_list = []
        self.taken = []
        self.fired = []
        self.counter = 0
        for x in range(self.size):
            self.board.append([SEA] * self.size)

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))

    def place_ship(self, ship, computer):
        for x in ship.dots:
            if x in self.taken or self.out_of_board(x):
                raise ShipPositioningException()
        for x in ship.dots:
            if not computer:
                self.board[x.x][x.y] = '@'
            self.taken.append(x)
        self.ships_list.append(ship)
        self.contour(ship, False)

    def place_ships(self, ships, size, computer):
        ship_count = 0
        for s in ships:
            for _ in range(0, 2000):
                ship = Ship(Dot(randint(0, size), randint(0, size)), s, randint(0, 1))
                try:
                    self.place_ship(ship, computer)
                    ship_count += 1
                    break
                except ShipPositioningException:
                    continue
        if ship_count < 7:
            self.__init__(size)
            self.place_ships(ships, size, computer)

    def out_of_board(self, dot) -> bool:
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for d in ship.dots:
            for dx, dy in near:
                if d == Dot(dx, dy):
                    continue
                dot = Dot(d.x + dx, d.y + dy)

                if not (self.out_of_board(dot)) and dot not in self.taken:
                    if verb:
                        self.board[dot.x][dot.y] = "."
                    self.taken.append(dot)

    def strike(self, dot, comp) -> bool:
        if self.out_of_board(dot):
            raise OutOfBoundariesException()

        if dot in self.fired:
            raise AlreadyUsedException()

        self.fired.append(dot)

        for s in self.ships_list:
            if dot in s.dots:
                s.lives -= 1
                self.board[dot.x][dot.y] = HIT
                if s.lives == 0:
                    self.counter += 1
                    self.contour(s, comp)
                    print("Terminated!")
                    return False
                else:
                    print("Damaged")
                    return True

        self.board[dot.x][dot.y] = FIRE
        print("Missed")
        return False
