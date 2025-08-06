from Map import GridPoint, build_stud_wall_grid_map_from_file, plot_path_on_grid_map
from PathFinder import AStarPathFinder
from Directions import create_orthogonal_movement

grid_map = build_stud_wall_grid_map_from_file("stud_walls_grid.tsv")

movement = create_orthogonal_movement()

start = GridPoint(50, 8)
goal = GridPoint(25, 92)

path_finder = AStarPathFinder(grid_map, start, goal, movement)
path = path_finder.find_path()
path_points = path.reconstruct_path()

if path_points:
    print(f"Path cost: {path.get_total_cost()}")
    print(f"Path length: {path.get_total_length()}")
    plot_path_on_grid_map(grid_map, start, goal, path_points)
else:
    print("No path found.")

del path_finder
del grid_map
del path