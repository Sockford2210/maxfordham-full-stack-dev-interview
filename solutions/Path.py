import math
from Directions import degrees_between_directions

#Entity to store entire path
class Path:
    def __init__(self, grid, movement):
        self.movement = movement
        self.grid = grid

    def setEndNode(self, end):
        self.end = end

    def getStartNode(self):
        node = self.end
        while node.parent:
            node = node.parent      
        return node

    def get_total_cost(self):
        return self.end.cost

    #Given a node returns the full array of parent nodes, inverted to return the start node first.
    def reconstruct_path(self):
        path_points = []
        node = self.end
        while node:
            path_points.append((node.y, node.x))
            node = node.parent
        return path_points[::-1]

    def get_direction_change_points(self):
        points = []
        node = self.end
        previous_node = None
        while node:
            if previous_node and previous_node.direction != node.direction:
                #Change to previous_node to return node with direction change rather than point of turn
                points.append((node.y, node.x))
            previous_node = node
            node = node.parent

        #Do not return start node point
        return points[:-1][::-1]

    def get_total_length(self):
        total_length = 0
        node = self.end
        while node and node.direction:
            total_length += node.direction.get_length()
            node = node.parent

        return total_length

class Node:
    def __init__(self, x, y, cost, heuristic, direction=None, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.direction = direction
        self.parent = parent

    #Make nodes comparable by cost plus heuristic for priority queue ordering
    #Heuristic - how far away from finish
    #Cost - cost spent up till this point
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)