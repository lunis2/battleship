class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, check):
        return self.x == check.x and self.y == check.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ship:
    def __init__(self, start_point, ship_len, orientation) -> None:
        self.start_point = start_point
        self.ship_len = ship_len
        self.orientation = orientation
        self.lives = ship_len

    @property
    def dots(self) -> list:
        ship_dots = []
        for i in range(self.ship_len):
            pos_x = self.start_point.x
            pos_y = self.start_point.y

            if self.orientation == 0:
                pos_x += i

            elif self.orientation == 1:
                pos_y += i

            else:
                raise ValueError

            ship_dots.append(Dot(pos_x, pos_y))

        return ship_dots
