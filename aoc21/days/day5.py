import os.path
import re


def day():
    puzzle_input = get_input()

    part1_floor_map = {}
    part2_floor_map = {}

    for line in puzzle_input:
        if line == "":
            break

        x1, y1, x2, y2 = [int(val) for val in re.findall("[\d]+", line)]

        horizontal_or_vertical = (x1 == x2) or (y1 == y2)

        for x, y in _get_range(x1, x2, y1, y2):
            if horizontal_or_vertical:
                part1_floor_map[(x, y)] = part1_floor_map.get((x, y), 0) + 1

            part2_floor_map[(x, y)] = part2_floor_map.get((x, y), 0) + 1

    print(
        f"Day 5 result 1 is {len([vents for _,vents in part1_floor_map.items() if vents > 1])}")
    print(
        f"Day 5 result 2 is {len([vents for _,vents in part2_floor_map.items() if vents > 1])}")


def _get_range(x1, x2, y1, y2):
    min_x, max_x = min(int(x1), int(x2)), max(int(x1), int(x2))
    min_y, max_y = min(int(y1), int(
        y2)), max(int(y1), int(y2))

    if min_x == max_x:  # x-level
        line_length = max_y - min_y
        return [(min_x, min_y + i) for i in range(0, line_length + 1)]

    elif min_y == max_y:  # y-level
        line_length = max_x - min_x
        return [(min_x + i, min_y) for i in range(0, line_length + 1)]

    elif (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):  # diagonal \
        line_length = max_x - min_x
        return [(min_x + i, min_y + i) for i in range(0, line_length + 1)]

    else:  # diagonal /
        line_length = max_x - min_x
        return [(min_x + i, max_y - i) for i in range(0, line_length + 1)]


def get_input():
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day5.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
