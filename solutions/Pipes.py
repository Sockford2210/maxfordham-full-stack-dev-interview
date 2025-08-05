import fluids
import math
from Directions import degrees_between_directions


#Normal fluid properties for room temperature water
DYNAMIC_VISCOSITY = 1E-3
FLUID_DENSITY = 1000

class Piping:
    def __init__(self):
        self.bends = []
        self.straight_sections = []

    def add_bend(bend):
        self.bends.append(bend)

    def add_straight_section(section):
        self.straight_sections.append(section)

class Bend:
    def __init__(self, x, y, degrees):
        self.x = x
        self.y = y
        self.degrees = degrees

class StraightSection:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def get_length(self):
        delta_x = abs(self.x2 - self.x1)
        delta_y = abs(self.y2 - self.y1)
        return math.sqrt(delta_x**2 + delta_y**2)

def get_bends_in_path(path):
    bends = []
    node = path.end
    previous_node = None
    while node:
        if previous_node and node.direction and previous_node.direction != node.direction:
            degrees_difference = degrees_between_directions(previous_node.direction, node.direction)
            bend = Bend(node.x, node.y, degrees_difference)
            bends.append(bend)
        previous_node = node
        node = node.parent

    return bends[::-1]

def get_straight_sections_in_path(path):
    straight_sections = []
    node = path.end
    previous_node = None
    x2 = node.x
    y2 = node.y
    while node:
        if previous_node and previous_node.direction != node.direction:
            #Should this be previous_node?
            x1 = node.x
            y1 = node.y
            section = StraightSection(x1, y1, x2, y2)
            straight_sections.append(section)

            x2 = node.x
            y2 = node.y
        previous_node = node
        node = node.parent

    return straight_sections[::-1]
