import math

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

def build_directions(direction_definitions):
    directions = set()
    for name, (dy, dx) in direction_definitions.items():
        direction = Direction(name, dx, dy)
        directions.add(direction)

    return directions

class Direction:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)

#Returns manhatten heuristic for a given node
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def chebyshev_distance(x1, y1, x2, y2):
    x_dif = abs(x1 - x2)
    y_dif = abs(y1 - y2)
    return max(x_dif, y_dif)

class Movement:
    def __init__(self):
        self.directions = build_directions(OTHOGONAL_DIRECTIONS)

    def distance(self, x1, y1, x2, y2):
        return manhattan_distance(x1, y1, x2, y2)

class OrthogonalMovement(Movement):
    pass

class DiagonalMovement(Movement):
    def __init__(self):
        self.directions = build_directions(DIAGONAL_DIRECTIONS)

    def distance(self, x1, y1, x2, y2):
        return chebyshev_distance(x1, y1, x2, y2)

def create_orthogonal_movement():
    return OrthogonalMovement()

def create_diagonal_movement():
    return DiagonalMovement()
    
def degrees_between_directions(direction1, direction2):
    dot = direction1.x*direction2.x + direction1.y*direction2.y
    mag1 = math.sqrt(direction1.x**2 + direction1.y**2)
    mag2 = math.sqrt(direction2.x**2 + direction2.y**2)

    cos_theta = dot / (mag1 * mag2)
    angle_rad = math.acos(cos_theta)
    angle_deg = math.degrees(angle_rad)

    return round(angle_deg)