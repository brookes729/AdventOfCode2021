import os.path
from math import prod


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    grid = {}
    column_length = 0

    for line in puzzle_input:
        if line == "":
            break

        line_values = list(line)
        for index, value in enumerate(line_values):
            grid[(column_length, index)] = int(value)

        column_length = column_length + 1

    for step in range(0, 10000):
        if sum(grid.values()) == 0:
            part_2_total = step
            break

        octopus_flashing = []
        increasing = list(grid.keys())

        while len(increasing) > 0:
            (x, y), increasing = increasing[0], increasing[1:]
            if (x, y) in octopus_flashing or (x, y) not in grid:
                continue
            if grid[(x, y)] == 9:
                if step < 100:
                    part_1_total = part_1_total + 1
                octopus_flashing = octopus_flashing + [(x, y)]
                grid[x, y] = 0
                increasing = increasing + \
                    [(x + 1, y-1), (x + 1, y), (x + 1, y+1),
                     (x, y-1), (x, y+1),
                     (x-1, y-1), (x-1, y), (x-1, y+1)]
            else:
                grid[x, y] = grid[x, y] + 1

    print(
        f"Day 9 result 1 is {part_1_total}")
    print(
        f"Day 9 result 2 is {part_2_total}")


def get_input():
    # yield from ["11111", "19991", "19191", "19991", "11111"]
    # yield from ["5483143223",
    #             "2745854711",
    #             "5264556173",
    #             "6141336146",
    #             "6357385478",
    #             "4167524645",
    #             "2176841721",
    #             "6882881134",
    #             "4846848554",
    #             "5283751526"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day11.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
