import math
from fluids import *
from Directions import degrees_between_directions

#Normal fluid properties for room temperature water
DYNAMIC_VISCOSITY = 1E-3
FLUID_DENSITY = 1000

class Piping:
    def __init__(self, diameter, roughness):
        self.diameter = diameter
        self.roughness = roughness
        self.bends = []
        self.straight_sections = []

    def set_bends(self, bends):
        self.bends = bends

    def set_straight_sections(self, sections):
        self.straight_sections = sections

    def get_total_length(self):
        length = 0
        for section in self.straight_sections:
            length += section.get_length()
        return length

    def calculate_water_pressure_drop(self, velocity):
        length = self.get_total_length()

        #Reynolds number is a property of the liquid flow
        #Re = (rho * V * D) / mu
        #rho: fluid density (kg/m3) - 1000kg/m3 normal for water
        #V: velocity (m/s)
        #D: pipe diameter (m)
        #mu: dynamic viscosity (N.s/m2) - 1E-3 typical for water at room temperature
        Re = Reynolds(V=velocity, D=self.diameter, rho=self.roughness, mu=DYNAMIC_VISCOSITY)

        #Friction factor of pipe
        fd = friction_factor(Re, eD=relative_roughness)

        #K is "dimensionless total loss coefficient" - refers to the the energy loss due to friction and changes (bends) in the pipe.
        K = K_from_f(fd=fd, L=length, D=self.diameter)

        #Assume normal entrance and exit
        K += entrance_sharp()
        K += exit_normal()
        
        for bend in self.bends:
            K += bend_rounded(Di=self.diameter, angle=bend.degrees, fd=fd)
        
        dp = dP_from_K(K, rho=self.roughness, V=velocity)
        return dp

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

def convert_path_to_piping(path, diameter, roughness):
    piping = Piping(diameter, roughness)

    bends = get_bends_in_path(path)
    piping.set_bends(bends)

    straight_sections = get_straight_sections_in_path(path)
    piping.set_straight_sections(straight_sections)

    return piping

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
