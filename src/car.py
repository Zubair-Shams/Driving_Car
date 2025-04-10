# car.py

class Car:
    # Directions in clockwise order for rotation
    DIRECTIONS = ['N', 'E', 'S', 'W']

    # Mapping for forward movement in each direction
    MOVES = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, name, x, y, direction):
        self.name = name              # Car's name (unique)
        self.x = x                    # X-coordinate
        self.y = y                    # Y-coordinate
        self.direction = direction    # Direction: N, E, S, W
        self.active = True            # True unless collision happens

    def rotate_left(self):
        """Rotate the car 90 degrees to the left."""
        idx = (Car.DIRECTIONS.index(self.direction) - 1) % 4
        self.direction = Car.DIRECTIONS[idx]

    def rotate_right(self):
        """Rotate the car 90 degrees to the right."""
        idx = (Car.DIRECTIONS.index(self.direction) + 1) % 4
        self.direction = Car.DIRECTIONS[idx]

    def move_forward(self):
        """Calculate the next position if moving forward."""
        dx, dy = Car.MOVES[self.direction]
        return self.x + dx, self.y + dy

    def update_position(self, new_x, new_y):
        """Update the car’s position."""
        self.x = new_x
        self.y = new_y

    def get_position(self):
        """Return (x, y, direction)"""
        return self.x, self.y, self.direction

    def __repr__(self):
        return f"{self.name} at ({self.x}, {self.y}) facing {self.direction}"
