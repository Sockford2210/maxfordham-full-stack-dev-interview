from Map import GridPoint, build_standard_grid_map_from_file, plot_path_on_grid_map
from PathFinder import AStarPathFinder
from Directions import create_diagonal_movement

grid_map = build_standard_grid_map_from_file("grid.tsv")

movement = create_diagonal_movement()

#Define start and end
start = GridPoint(40, 18)
goal = GridPoint(25, 92)

path_finder = AStarPathFinder(grid_map, start, goal, movement)
path = path_finder.find_path()

if path:
    print(f"Path length: {len(path)}")
    plot_path_on_grid_map(grid_map, start, goal, path)
else:
    print("No path found.")

del path_finder
del grid_map