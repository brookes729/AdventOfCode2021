import os.path
from statistics import median, mean
from math import floor, ceil


def day():
    puzzle_input = [int(crab)
                    for crab in next(get_input()).split(",")]
    target_point_part1 = median(puzzle_input)

    # Could probably figure out why it is one or the other but for the sake of speed floor for the real one, ceil for the example
    target_point_part2_min = floor(mean(puzzle_input))
    target_point_part2_max = ceil(mean(puzzle_input))

    # Triangle numbers formula
    part2_position_fuel = [sum(
        [int(abs(position - crab)*(abs(position - crab)+1)/2) for crab in puzzle_input])
        for position in [target_point_part2_min, target_point_part2_max]]

    print(
        f"Day 7 result 1 is {sum([abs(target_point_part1 - crab) for crab in puzzle_input])}")
    print(
        f"Day 7 result 2 is {min([value for value in part2_position_fuel])}")


def get_input():
    # yield "16,1,2,0,4,2,7,1,2,14"
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day7.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
