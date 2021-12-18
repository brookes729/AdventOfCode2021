import os.path
from copy import deepcopy


class snail_number:
    def __init__(self, first_value, second_value, is_snail, depth):
        self.first_value = first_value
        self.second_value = second_value
        self.is_snail = is_snail
        self.depth = depth

    def is_explodable(self):
        return self.max_depth() > 4

    def is_splittable(self):
        return self.max_value() > 9

    def max_depth(self):
        if not self.is_snail:
            return self.depth
        else:
            return max(self.first_value.max_depth(), self.second_value.max_depth())

    def max_value(self):
        if not self.is_snail:
            return self.first_value
        else:
            return max(self.first_value.max_value(), self.second_value.max_value())

    def explode(self):
        first, second = 0, 0
        if self.depth == self.max_depth() - 1 and self.depth > 3:
            first, second = self.first_value.first_value, self.second_value.first_value
            self.first_value = 0
            self.second_value = 0
            self.is_snail = False
            return (first, second)
        elif self.depth == self.max_depth() - 1:
            return (0, 0)
        if self.first_value.is_snail and self.first_value.max_depth() > 4:
            (first, second) = self.first_value.explode()
            if self.second_value.is_snail:
                self.second_value.add_first(second)
            else:
                self.second_value.first_value = self.second_value.first_value + second
            return (first, 0)
        if self.second_value.is_snail and self.second_value.max_depth() > 4:
            (first, second) = self.second_value.explode()
            if self.first_value.is_snail:
                self.first_value.add_second(first)
            else:
                self.first_value.first_value = self.first_value.first_value + first
            return (0, second)

    def add_first(self, value):
        if self.first_value.is_snail:
            self.first_value.add_first(value)
        else:
            self.first_value.first_value = self.first_value.first_value + value

    def add_second(self, value):
        if self.second_value.is_snail:
            self.second_value.add_second(value)
        else:
            self.second_value.first_value = self.second_value.first_value + value

    def split(self):
        if not self.is_snail:
            if self.first_value > 9:
                self.is_snail = True
                value = self.first_value
                self.first_value = snail_number(
                    int(value / 2), None, False, self.depth + 1)
                self.second_value = snail_number(
                    int(value / 2) + value % 2, None, False, self.depth + 1)
        else:
            if self.first_value.is_splittable():
                self.first_value.split()
            elif self.second_value.is_splittable():
                self.second_value.split()

    def increase_depth(self):
        self.depth = self.depth + 1
        if self.is_snail:
            self.first_value.increase_depth()
            self.second_value.increase_depth()

    def magnitude(self):
        if not self.is_snail:
            return self.first_value
        return (3 * self.first_value.magnitude()) + (2 * self.second_value.magnitude())

    def __repr__(self):
        if not self.is_snail:
            return str(self.first_value)
        return f"[{self.first_value},{self.second_value}]"


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    inputs = []
    first_input = _build_snail_number(next(puzzle_input), 0)
    running_total = deepcopy(first_input)
    first_input.increase_depth()
    inputs.append(first_input)

    for sum in puzzle_input:
        if sum == "":
            break

        new_value = _build_snail_number(sum, 1)
        inputs.append(deepcopy(new_value))

        running_total.increase_depth()

        running_total = _reduce(snail_number(
            running_total, deepcopy(new_value), True, 0))

    for first_number in inputs:
        for second_number in inputs:
            if str(first_number) == str(second_number):
                continue
            new_magnitude = _reduce(snail_number(
                deepcopy(first_number), deepcopy(second_number), True, 0)).magnitude()
            if new_magnitude > part_2_total:
                part_2_total = new_magnitude

    print(
        f"Day 16 result 1 is {running_total.magnitude()}")

    print(
        f"Day 16 result 2 is: {part_2_total}")


def _build_snail_number(string_input, depth):
    if string_input.isnumeric():
        return snail_number(int(string_input), 0, False, depth)
    else:
        first_value = ""
        current_value = ""
        string_depth = 0
        for character in string_input[1:-1]:
            current_value = current_value + character
            if character == "[":
                string_depth = string_depth + 1
            elif character == "]":
                string_depth = string_depth - 1
            elif character == "," and string_depth == 0:
                first_value, current_value = current_value[:-1], ""
        return snail_number(_build_snail_number(first_value, depth + 1), _build_snail_number(current_value, depth + 1), True, depth)


def _reduce(snail_number):
    while True:
        if snail_number.is_explodable():
            snail_number.explode()
        elif snail_number.is_splittable():
            snail_number.split()
        else:
            break
    return snail_number


def get_input():
    # Reduce tests
    # yield from ["[[[[[9,8],1],2],3],4]"]
    # yield from ["[7,[6,[5,[4,[3,2]]]]]"]
    # yield from ["[[6,[5,[4,[3,2]]]],1]"]
    # yield from ["[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"]
    # yield from ["[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"]
    # yield from ["[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"]

    # yield from ["[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]"]

    # yield from ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"]

    # yield from ["[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
    #             "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
    #             "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
    #             "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
    #             "[7,[5,[[3,8],[1,4]]]]",
    #             "[[2,[2,2]],[8,[8,1]]]",
    #             "[2,9]",
    #             "[1,[[[9,3],9],[[9,0],[0,7]]]]",
    #             "[[[5,[7,4]],7],1]",
    #             "[[[[4,2],2],6],[8,7]]"]

    # yield from ["[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
    #             "[[[5,[2,8]],4],[5,[[9,9],0]]]",
    #             "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
    #             "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
    #             "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
    #             "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
    #             "[[[[5,4],[7,7]],8],[[8,3],8]]",
    #             "[[9,3],[[9,9],[6,[4,9]]]]",
    #             "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    #             "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day18.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
