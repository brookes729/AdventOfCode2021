import os.path
from math import prod


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    paper = set()

    for dot in puzzle_input:
        if dot == "":
            break

        x, y = dot.split(",")
        paper.add((int(x), int(y)))

    first_fold = next(puzzle_input).split("fold along ")[1]
    axis, value = first_fold.split("=")
    if axis == "x":
        paper = set([dot for dot in paper if
                     dot[0] <= int(value)]).union(
            set([((2*int(value)) - dot[0], dot[1]) for dot in paper if
                 dot[0] > int(value)]))
    else:
        paper = set([dot for dot in paper if
                     dot[1] <= int(value)]).union(
            set([(dot[0], (2*int(value)) - dot[1]) for dot in paper if
                 dot[1] > int(value)]))

    part_1_total = len(paper)

    for fold in puzzle_input:
        if fold == "":
            break

        axis, value = fold.split("fold along ")[1].split("=")
        if axis == "x":
            paper = set([dot for dot in paper if
                        dot[0] <= int(value)]).union(
                set([((2*int(value)) - dot[0], dot[1]) for dot in paper if
                    dot[0] > int(value)]))
        else:
            paper = set([dot for dot in paper if
                        dot[1] <= int(value)]).union(
                set([(dot[0], (2*int(value)) - dot[1]) for dot in paper if
                    dot[1] > int(value)]))

    print(
        f"Day 9 result 1 is {part_1_total}")
    print(
        f"Day 9 result 2 is:")

    _visualise_paper(paper)


def _visualise_paper(paper):
    x_max, y_max = max([dot[0] for dot in paper]), max(
        [dot[1] for dot in paper])

    for y in range(0, y_max + 1):
        line = ""
        for x in range(0, x_max + 1):
            if (x, y) in paper:
                line = line + "#"
            else:
                line = line + " "
        print(line)


def get_input():
    # yield from ["6,10",
    #             "0,14",
    #             "9,10",
    #             "0,3",
    #             "10,4",
    #             "4,11",
    #             "6,0",
    #             "6,12",
    #             "4,1",
    #             "0,13",
    #             "10,12",
    #             "3,4",
    #             "3,0",
    #             "8,4",
    #             "1,10",
    #             "2,14",
    #             "8,10",
    #             "9,0",
    #             "",
    #             "fold along y=7",
    #             "fold along x=5"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day13.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
