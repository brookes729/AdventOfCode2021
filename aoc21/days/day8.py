import os.path


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    for line in puzzle_input:
        if line == "":
            break

        numbers, results = [segment.strip().split(" ")
                            for segment in line.split(" | ")]

        part_1_total = part_1_total + \
            sum([1 for result in results if len(result) in [2, 3, 4, 7]])

        translation = {}
        translation[1] = [''.join(sorted(number))
                          for number in numbers if len(number) == 2][0]
        translation[7] = [''.join(sorted(number))
                          for number in numbers if len(number) == 3][0]
        translation[4] = [''.join(sorted(number))
                          for number in numbers if len(number) == 4][0]
        translation[8] = [''.join(sorted(number))
                          for number in numbers if len(number) == 7][0]
        translation[6] = [''.join(sorted(number))
                          for number in numbers if len(number) == 6
                          and not set(translation[1]).issubset(set(number))][0]
        translation[9] = [''.join(sorted(number))
                          for number in numbers if len(number) == 6
                          and set(translation[4]).issubset(set(number))][0]
        translation[0] = [''.join(sorted(number))
                          for number in numbers if len(number) == 6
                          and not set(translation[9]).issubset(set(number))
                          and not set(translation[6]).issubset(set(number))][0]
        translation[5] = [''.join(sorted(number))
                          for number in numbers if len(number) == 5
                          and set(number).issubset(set(translation[6]))][0]
        translation[3] = [''.join(sorted(number))
                          for number in numbers if len(number) == 5
                          and set(translation[1]).issubset(set(number))][0]
        translation[2] = [''.join(sorted(number))
                          for number in numbers if len(number) == 5
                          and not set(translation[5]).issubset(set(number))
                          and not set(translation[3]).issubset(set(number))][0]

        reversed_translation = {v: k for k, v in translation.items()}

        part_2_total = part_2_total + \
            int("".join([str(reversed_translation[''.join(sorted(number))])
                for number in results]))

    print(
        f"Day 8 result 1 is {part_1_total}")
    print(
        f"Day 8 result 2 is {part_2_total}")


def get_input():
    # yield "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    # yield from ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n",
    #             "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n",
    #             "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n",
    #             "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n",
    #             "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n",
    #             "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n",
    #             "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n",
    #             "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n",
    #             "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n",
    #             "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day8.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
