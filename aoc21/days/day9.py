import os.path
from math import prod


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    grid = {}
    grid_min = {}
    row_length = 0
    column_length = 0

    basins = []

    for line in puzzle_input:
        if line == "":
            break

        line_values = list(line)
        row_length = len(line_values)
        for index, value in enumerate(line_values):
            grid[(column_length, index)] = int(value)

        column_length = column_length + 1

    for x, y in grid.keys():
        grid_min[(x, y)] = grid[(x, y)] < grid.get((x - 1, y), 10) and \
            grid[(x, y)] < grid.get((x + 1, y), 10) and \
            grid[(x, y)] < grid.get((x, y - 1), 10) and \
            grid[(x, y)] < grid.get((x, y + 1), 10)

        if grid_min[(x, y)]:
            part_1_total = part_1_total + grid[(x, y)] + 1

            basins = basins + [_find_basin_size(grid, x, y)]

    print(
        f"Day 9 result 1 is {part_1_total}")
    print(
        f"Day 9 result 2 is {prod(sorted(basins, reverse=True)[:3])}")


def _find_basin_size(grid, x, y):
    basin = [(x, y)]
    basin_to_check = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    while len(basin_to_check) > 0:
        next_check, basin_to_check = basin_to_check[0], basin_to_check[1:]

        if grid.get(next_check, 9) != 9 and not next_check in basin:
            basin = basin + [next_check]
            basin_to_check = basin_to_check + [(next_check[0] - 1, next_check[1]), (next_check[0] + 1, next_check[1]),
                                               (next_check[0], next_check[1] - 1), (next_check[0], next_check[1] + 1)]

    return len(basin)


def get_input():
    # yield from ["2199943210",
    #             "3987894921",
    #             "9856789892",
    #             "8767896789",
    #             "9899965678"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day9.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
