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

    global pair_step_result, pair_step_sum
    pair_step_result = {}
    pair_step_sum = {}
    for pair in puzzle_input:
        if pair == "":
            break

        pair = pair.split(" -> ")
        pairs[tuple(list(pair[0]))] = pair[1]
        pair_step_result[(pair[0], 1)] = pair[1] + pair[0][1]

    chemical_occurances = _process_string(chemical, 10)
    chemical_occurances[chemical[0]] = chemical_occurances[chemical[0]] + 1

    print(
        f"Day 14 result 1 is {max(chemical_occurances.values()) - min(chemical_occurances.values())}")

    chemical_occurances2 = _process_string(chemical, 40)
    chemical_occurances2[chemical[0]] = chemical_occurances2[chemical[0]] + 1

    print(
        f"Day 14 result 2 is: {max(chemical_occurances2.values()) - min(chemical_occurances2.values())}")


def _process_string(chemical, steps):
    count_of_molecules = {}

    for pair in list(zip(chemical, chemical[1:])):
        for molecule, value in _process_pair("".join(pair), steps).items():
            count_of_molecules[molecule] = count_of_molecules.get(
                molecule, 0) + value

    return count_of_molecules


def _process_pair(pair, steps):
    if not ("".join(pair), steps) in pair_step_sum:
        if ("".join(pair), steps) in pair_step_result:
            pair_step_sum[("".join(pair), steps)] = Counter(
                pair_step_result[("".join(pair), steps)])
        else:
            new_chemical = _process_string(
                pair[0] + pair_step_result[("".join(pair), 1)], steps - 1)
            pair_step_sum[("".join(pair), steps)] = Counter(new_chemical)

    return pair_step_sum[("".join(pair), steps)]


def get_input():
    # yield from ["NNCB",
    #             "",
    #             "CH -> B",
    #             "HH -> N",
    #             "CB -> H",
    #             "NH -> C",
    #             "HB -> C",
    #             "HC -> B",
    #             "HN -> C",
    #             "NN -> C",
    #             "BH -> H",
    #             "NC -> B",
    #             "NB -> B",
    #             "BN -> B",
    #             "BB -> N",
    #             "BC -> B",
    #             "CC -> N",
    #             "CN -> C"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day14.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
