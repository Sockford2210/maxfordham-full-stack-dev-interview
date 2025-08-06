import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path

#Encapsulates a point on a grid
class GridPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return int(((self.x + self.y)*(self.x + self.y + 1))/2 + self.y)

#Class to encapsulate a given grid matrix, with rules on what points can be penetrated#Grid is grid[y][x]
#Y increases top to bottom
#X Increases left to right
class GridMap:
    def __init__(self, grid):
        self.grid = grid

    def is_point_penetrable(self, x, y):
        return self.grid[y][x] != 1

    def is_point_within_grid(self, x, y):
        number_of_rows = len(self.grid) 
        number_of_columns = len(self.grid[0])

        if (0 <= x < number_of_columns) and (0 <= y < number_of_rows):
            return True
        else:
            return False

    def wall_cost(self, x, y):
        return self.grid[y][x]

#Implementation of GridMap with penetrable stud wall, inpenetrable walls have value 
#of 100.
class StudWallGridMap(GridMap):
    def is_point_penetrable(self, x, y):
        return self.grid[y][x] != 100

#Standard implementation of GridMap
class StandardGridMap(GridMap):
    pass

#Plots a grid map with start and goal points and optional direction change points
def plot_path_on_grid_map(grid_map, start, goal, path, direction_change_points=None):
    grid = grid_map.grid

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(grid, cmap=plt.cm.Dark2)
    ax.scatter(start.x, start.y, marker="*", color="yellow", s=200)
    ax.scatter(goal.x, goal.y, marker="*", color="red", s=200)

    if path:
        for i in range(1, len(path) - 1):
            ax.scatter(path[i][1], path[i][0], color="blue", s=10)

    if direction_change_points:
        for point in direction_change_points:
            ax.scatter(point[1], point[0], marker="^", color="green", s=50)
            
    plt.show()

#Imports a tsv/csv file and converts it to a grid matrix
def import_grid_matrix_from_file(filepath):
    rows = list(csv.reader(Path(filepath).open(encoding="utf-8"), delimiter="\t"))
    grid = np.array([[int(x) for x in row] for row in rows])

    return grid

#Builds a StandardGridMap from file
def build_standard_grid_map_from_file(filepath):
    grid = import_grid_matrix_from_file(filepath)

    grid_map = StandardGridMap(grid)
    return grid_map

#Builds a StudWallGridMap from file, walls (value=1) are converted to 100
#This is done primarily for plotting purposes.
def build_stud_wall_grid_map_from_file(filepath):
    grid = import_grid_matrix_from_file(filepath)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                grid[y][x] = 100

    grid_map = StudWallGridMap(grid)
    return grid_map