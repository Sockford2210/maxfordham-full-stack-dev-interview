from Directions import build_directions, DIAGONAL_DIRECTIONS

directions = build_directions(DIAGONAL_DIRECTIONS)

for direction in directions:
    print(direction.name + ": {" + str(direction.x) + "," + str(direction.y) + "}, length: " + str(direction.get_length()))