import os.path
from time import process_time


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    grid = {}
    grid_min = {}
    row = 0

    for line in puzzle_input:
        if line == "":
            break

        for index, height in enumerate(line):
            grid[(row, index)] = int(height)
            grid_min[(row, index)] = 99999

        row = row + 1

    grid2_mid = {}
    grid2 = {}
    grid2_min = {}
    for node in grid:
        grid2_mid[(node[0], node[1])] = grid[node]
        grid2_mid[(node[0], node[1] + row)] = (grid[node] +
                                               1) if (grid[node] + 1) <= 9 else (grid[node] + 1) % 9
        grid2_mid[(node[0], node[1] + 2 * row)] = (grid[node] +
                                                   2) if (grid[node] + 2) <= 9 else (grid[node] + 2) % 9
        grid2_mid[(node[0], node[1] + 3 * row)] = (grid[node] +
                                                   3) if (grid[node] + 3) <= 9 else (grid[node] + 3) % 9
        grid2_mid[(node[0], node[1] + 4 * row)] = (grid[node] +
                                                   4) if (grid[node] + 4) <= 9 else (grid[node] + 4) % 9
    for node in grid2_mid:
        grid2[(node[0], node[1])] = grid2_mid[node]
        grid2[(node[0] + row, node[1])] = (grid2_mid[node] +
                                           1) if (grid2_mid[node] + 1) <= 9 else (grid2_mid[node] + 1) % 9
        grid2[(node[0] + 2 * row, node[1])] = (grid2_mid[node] +
                                               2) if (grid2_mid[node] + 2) <= 9 else (grid2_mid[node] + 2) % 9
        grid2[(node[0] + 3 * row, node[1])] = (grid2_mid[node] +
                                               3) if (grid2_mid[node] + 3) <= 9 else (grid2_mid[node] + 3) % 9
        grid2[(node[0] + 4 * row, node[1])] = (grid2_mid[node] +
                                               4) if (grid2_mid[node] + 4) <= 9 else (grid2_mid[node] + 4) % 9

    for x in range(row * 5):
        for y in range(row * 5):
            grid2_min[(x, y)] = 99999

    target = (row - 1, index)

    _find_path(grid, grid_min, target)

    print(f"Day 14 result 1 is {grid_min[target]}")

    target = ((5 * row) - 1, (5 * row) - 1)

    start = process_time()
    _find_path(grid2, grid2_min, target)
    end = process_time()
    print(f"Day 14 result 2 is: {grid2_min[target]} taking {end - start}s")


def _find_path(grid, grid_min, target):
    to_visit_dict = {0: [(0, 0)]}
    visited = []

    grid[(0, 0)] = 0
    grid_min[(0, 0)] = 0

    while grid_min[target] == 99999:
        next_nodes = to_visit_dict.pop(min(list(to_visit_dict.keys())))

        for next_node in next_nodes:
            if next_node in visited:
                continue

            visited = visited + [next_node]

            for neighbour in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbour_node = (
                    next_node[0] + neighbour[0], next_node[1] + neighbour[1])
                if not neighbour_node in grid.keys():
                    continue

                potential_min = grid[neighbour_node] + grid_min[next_node]

                if (potential_min >= grid_min[neighbour_node]):
                    continue

                grid_min[neighbour_node] = potential_min

                if not neighbour_node in visited:
                    neighbour_weight = grid_min[neighbour_node] + \
                        sum(target) - sum(neighbour_node)
                    if not neighbour_node in to_visit_dict.get(neighbour_weight, []):
                        to_visit_dict[neighbour_weight] = to_visit_dict.get(
                            neighbour_weight, []) + [neighbour_node]


def get_input():
    # yield from ["1163751742",
    #             "1381373672",
    #             "2136511328",
    #             "3694931569",
    #             "7463417111",
    #             "1319128137",
    #             "1359912421",
    #             "3125421639",
    #             "1293138521",
    #             "2311944581"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day15.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
