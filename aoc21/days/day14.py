import os.path
from collections import Counter


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    pairs = {}
    chemical = list(next(puzzle_input))
    chemical_pairs = list(zip(chemical, chemical[1:]))

    next(puzzle_input)  # Blank line after chemical

    global pair_step_result
    pair_step_result = {}
    for pair in puzzle_input:
        if pair == "":
            break

        pair = pair.split(" -> ")
        pairs[tuple(list(pair[0]))] = pair[1]
        pair_step_result[(pair[0], 1)] = pair[1] + pair[0][1]

    test_chemical10 = chemical[0] + "".join(_process_string(chemical, 10))
    test_chemical40 = chemical[0] + "".join(_process_string(chemical, 40))

    chemical_occurances = Counter(test_chemical10)
    chemical_occurances2 = Counter(test_chemical40)

    print(
        f"Day 14 result 1 is {max(chemical_occurances.values()) - min(chemical_occurances.values())}")
    print(
        f"Day 14 result 2 is: {max(chemical_occurances2.values()) - min(chemical_occurances2.values())}")


def _process_string(chemical, steps):
    new_chemical = []

    for pair in list(zip(chemical, chemical[1:])):
        new_chemical = new_chemical + [_process_pair("".join(pair), steps)]

    return new_chemical


def _process_pair(pair, steps):
    if not ("".join(pair), steps) in pair_step_result:
        new_chemical = _process_string(
            pair[0] + pair_step_result[(pair, 1)], steps - 1)
        pair_step_result[("".join(pair), steps)] = "".join(new_chemical)

    return pair_step_result[("".join(pair), steps)]


def get_input():
    yield from ["NNCB",
                "",
                "CH -> B",
                "HH -> N",
                "CB -> H",
                "NH -> C",
                "HB -> C",
                "HC -> B",
                "HN -> C",
                "NN -> C",
                "BH -> H",
                "NC -> B",
                "NB -> B",
                "BN -> B",
                "BB -> N",
                "BC -> B",
                "CC -> N",
                "CN -> C"]

    # try:
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../../test_inputs/day14.txt")
    #     file1 = open(path, 'r')
    #     while True:
    #         yield file1.readline().strip()
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    day()
