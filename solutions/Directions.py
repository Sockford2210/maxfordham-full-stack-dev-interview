# Define orthogonal directions
OTHOGONAL_DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

DIAGONAL_DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up-left': (-1, -1),
    'up-right': (-1, 1),
    'down-left': (1, -1),
    'down-right': (1, 1),
}

#Returns manhatten heuristic for a given node
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def chebyshev_distance(x1, y1, x2, y2):
    x_dif = abs(x1 - x2)
    y_dif = abs(y1 - y2)
    return max(x_dif, y_dif)

class Movement:
    def __init__(self):
        self.directions = OTHOGONAL_DIRECTIONS

    def distance(self, x1, y1, x2, y2):
        return manhattan_distance(x1, y1, x2, y2)

class OrthogonalMovement(Movement):
    pass

class DiagonalMovement(Movement):
    def __init__(self):
        self.directions = DIAGONAL_DIRECTIONS

    def distance(self, x1, y1, x2, y2):
        return chebyshev_distance(x1, y1, x2, y2)

def create_orthogonal_movement():
    return OrthogonalMovement()

def create_diagonal_movement():
    return DiagonalMovement()