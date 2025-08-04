from Map import GridPoint, build_stud_wall_grid_map_from_file, plot_path_on_grid_map
from PathFinder import AStarPathFinder
from Directions import create_orthogonal_movement

grid_map = build_stud_wall_grid_map_from_file("stud_walls_grid.tsv")

movement = create_orthogonal_movement()

#Define start and end
start = GridPoint(50, 8)
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