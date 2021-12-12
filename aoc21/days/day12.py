import os.path
from math import prod


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    global links
    links = {}

    for line in puzzle_input:
        if line == "":
            break

        start, end = line.split("-")
        links[start] = links.get(start, []) + [end]
        links[end] = links.get(end, []) + [start]

    part_1_total = len(_traverse_map("start", ["start"]))
    part_2_total = len(_traverse_map2("start", ["start"], False))

    print(
        f"Day 9 result 1 is {part_1_total}")
    print(
        f"Day 9 result 2 is {part_2_total}")


def _traverse_map(starting_point, path_so_far):
    result = []
    for next_step in links[starting_point]:
        if next_step == "end":
            result = result + [path_so_far + [next_step]]
        elif not (next_step in path_so_far) or next_step.isupper():
            for path in _traverse_map(next_step, path_so_far + [next_step]):
                if len(path) > 0:
                    result = result + [path]
    return result


def _traverse_map2(starting_point, path_so_far, twice_visited):
    result = []
    for next_step in links[starting_point]:
        if next_step == "end":
            result = result + [path_so_far + [next_step]]
        elif next_step != "start" and next_step in path_so_far and next_step.islower() and not twice_visited:
            for path in _traverse_map2(next_step, path_so_far + [next_step], True):
                if len(path) > 0:
                    result = result + [path]
        elif next_step != "start" and not (next_step in path_so_far) or next_step.isupper():
            for path in _traverse_map2(next_step, path_so_far + [next_step], twice_visited):
                if len(path) > 0:
                    result = result + [path]
    return result


def get_input():
    # yield from ["start-A",
    #             "start-b",
    #             "A-c",
    #             "A-b",
    #             "b-d",
    #             "A-end",
    #             "b-end"]
    # yield from ["dc-end",
    #             "HN-start",
    #             "start-kj",
    #             "dc-start",
    #             "dc-HN",
    #             "LN-dc",
    #             "HN-end",
    #             "kj-sa",
    #             "kj-HN",
    #             "kj-dc"]
    # yield from ["fs-end",
    #             "he-DX",
    #             "fs-he",
    #             "start-DX",
    #             "pj-DX",
    #             "end-zg",
    #             "zg-sl",
    #             "zg-pj",
    #             "pj-he",
    #             "RW-he",
    #             "fs-DX",
    #             "pj-RW",
    #             "zg-RW",
    #             "start-pj",
    #             "he-WI",
    #             "zg-he",
    #             "pj-fs",
    #             "start-RW"]
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day12.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
