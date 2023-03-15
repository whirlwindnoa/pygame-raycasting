from config import Config

# WALL IS #
# EMPTY SPACE IS .
map1 = [
    "############",
    "#..........#",
    "####....####",
    "#..........#",
    "#..........#",
    "####....####",
    "#..........#",
    "############"
]

map2 = [
    "############",
    "#.#..##..#.#",
    "#..........#",
    "#...#..#...#",
    "#...#..#...#",
    "#..........#",
    "#.#..##..#.#",
    "############"
]
current_map = map2

world_map = set()
for j, row in enumerate(current_map):
    for i, char in enumerate(row):
        if char == "#":
            world_map.add((i * Config.TILE, j * Config.TILE))
        print(i, j)
