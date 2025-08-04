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

#Given a node returns the full array of parent nodes, inverted to return the start node first.
def reconstruct_path(node):
    path = []
    while node:
        path.append((node.y, node.x))
        node = node.parent
    return path[::-1]