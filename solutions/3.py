from Map import GridPoint, build_standard_grid_map_from_file, plot_path_on_grid_map
from PathFinder import AStarPathFinder
from Directions import create_orthogonal_movement
from Pipes import get_bends_in_path, get_straight_sections_in_path
grid_map = build_standard_grid_map_from_file("grid.tsv")

movement = create_orthogonal_movement()

#Define start and end
start = GridPoint(40, 18)
goal = GridPoint(25, 92)

path_finder = AStarPathFinder(grid_map, start, goal, movement)
path = path_finder.find_path()
path_points = path.reconstruct_path()
direction_change_points = path.get_direction_change_points()

bends = get_bends_in_path(path)
straight_sections = get_straight_sections_in_path(path)

if path:
    print(f"Path cost: {path.get_total_cost()}")
    print(f"Path length: {path.get_total_length()}")
    plot_path_on_grid_map(grid_map, start, goal, path_points, direction_change_points)

    for straight in straight_sections:
        print(f"Straight: ({straight.x1},{straight.y1} : {straight.x2},{straight.y2}), length: {straight.get_length()}")

    for bend in bends:
        print(f"Bend: ({bend.x},{bend.y}), degrees: {bend.degrees}")
else:
    print("No path found.")

del path_finder
del grid_map