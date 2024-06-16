# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"


class Robot:

    _compass = [WEST, NORTH, EAST, SOUTH]

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = int(x_pos)
        self.y_pos = int(y_pos)
        self.index = self._compass.index(direction)

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def move(self, d):
        for order in list(d):
            match order:
                case "A":
                    match self.direction:
                        case "north":
                            self.y_pos += 1
                        case "south":
                            self.y_pos -= 1
                        case "west":
                            self.x_pos -= 1
                        case "east":
                            self.x_pos += 1

                case "L":
                    self.index = 3 if self.index == 0 else self.index - 1

                case "R":
                    self.index = 0 if self.index == 3 else self.index + 1

            self.direction = self._compass[self.index]
