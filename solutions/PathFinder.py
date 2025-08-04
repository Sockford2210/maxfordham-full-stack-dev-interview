import heapq
from Node import Node, reconstruct_path
from Directions import manhattan_distance
from Map import GridPoint, GridMap

CHANGE_DIRECTION_COST = 2
BASE_MOVE_COST = 1

class AStarPathFinder:
    def __init__(self, grid_map, start, goal, movement):
        self.grid_map = grid_map
        self.start = start
        self.goal = goal
        self.movement = movement
        self.visited_points = set()
        self.node_queue = []

    def find_path(self):
        start_heuristic = self.movement.distance(self.start.x, self.start.y, self.goal.x, self.goal.y)
        start_node = Node(self.start.x, self.start.y, 0, start_heuristic)

        self.add_next_directions_to_queue(start_node)

        while self.node_queue:
            current_node = heapq.heappop(self.node_queue)

            point = GridPoint(current_node.x, current_node.y)
            if point in self.visited_points:
                continue
            
            self.visited_points.add(point)

            if point == self.goal:
                return current_node

            self.add_next_directions_to_queue(current_node)

        return None


    def add_next_directions_to_queue(self, current_node):
        for direction, (dy, dx) in self.movement.directions.items():
            delta = GridPoint(dx, dy)
            new_x = current_node.x + delta.x
            new_y = current_node.y + delta.y

            if self.grid_map.is_point_within_grid(new_x, new_y) and self.grid_map.is_point_penetrable(new_x, new_y):
                new_cost = current_node.cost + BASE_MOVE_COST + self.grid_map.wall_cost(new_x, new_y)
                if direction != current_node.direction:
                    new_cost += CHANGE_DIRECTION_COST
                heuristic = self.movement.distance(new_x, new_y, self.goal.x, self.goal.y)
                new_node = Node(new_x, new_y, new_cost, heuristic, direction, current_node)
                heapq.heappush(self.node_queue, new_node)