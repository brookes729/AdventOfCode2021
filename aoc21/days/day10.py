import os.path
from re import subn, search
from math import floor


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    part_1_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    part_2_score = {"(": 1, "[": 2, "{": 3, "<": 4}

    auto_complete_scores = []

    for line in puzzle_input:
        if line == "":
            break

        while len(line) > 0:
            line, changes = subn("\[\]|\(\)|\{\}|\<\>", "", line)

            if changes == 0:
                closing_bracket = search("[\]\>\)\}]", line)

                if closing_bracket != None:
                    part_1_total = part_1_total + \
                        part_1_score[line[closing_bracket.span()[0]]]
                else:
                    auto_complete = list(line)
                    auto_complete.reverse()
                    line_score = 0
                    for bracket in auto_complete:
                        line_score = (line_score * 5) + part_2_score[bracket]

                    auto_complete_scores = auto_complete_scores + [line_score]
                break

    auto_complete_scores.sort()
    part_2_total = auto_complete_scores[floor(len(auto_complete_scores) / 2)]

    print(
        f"Day 9 result 1 is {part_1_total}")
    print(
        f"Day 9 result 2 is {part_2_total}")


def get_input():
    # yield from ["[({(<(())[]>[[{[]{<()<>>",
    #             "[(()[<>])]({[<{<<[]>>(",
    #             "{([(<{}[<>[]}>{[]{[(<()>",
    #             "(((({<>}<{<{<>}{[]{[]{}",
    #             "[[<[([]))<([[{}[[()]]]",
    #             "[{[{({}]{}}([{[{{{}}([]",
    #             "{<[[]]>}<{[{[{[]{()[[[]",
    #             "[<(<(<(<{}))><([]([]()",
    #             "<{([([[(<>()){}]>(<<{{",
    #             "<{([{{}}[<[[[<>{}]]]>[]]"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day10.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
