import os.path
from math import prod


def day():
    puzzle_input = next(get_input())
    puzzle_input = bin(int(puzzle_input, 16))[2:].zfill(len(puzzle_input * 4))

    part_1_total = 0
    part_2_total = 0

    part_2_total, part_1_total, _ = _calculate_bytes(
        puzzle_input, part_1_total)

    print(
        f"Day 16 result 1 is {part_1_total}")

    print(
        f"Day 16 result 2 is: {part_2_total}")


def _calculate_bytes(puzzle_input, part_1_total):
    version, type, puzzle_input = puzzle_input[:
                                               3], puzzle_input[3:6], puzzle_input[6:]

    part_1_total = part_1_total + int(version, 2)

    value = 0

    if type == "100":
        value = ""
        buffer_length = 2
        while True:
            check, next_number, puzzle_input = puzzle_input[0], puzzle_input[1:5], puzzle_input[5:]

            value = value + next_number
            buffer_length = (buffer_length + 3) % 4
            if check == '0':
                break
        value = int(value, 2)
    else:
        buffer_length = 1
        length_type, puzzle_input = puzzle_input[0], puzzle_input[1:]
        if length_type == '0':
            length, puzzle_input = puzzle_input[:15], puzzle_input[15:]
            sub_packets, puzzle_input = puzzle_input[:int(
                length, 2)], puzzle_input[int(length, 2):]
            value_array = []
            while int('0' + sub_packets, 2) > 0:
                new_value, part_1_total, sub_packets = _calculate_bytes(
                    sub_packets, part_1_total)
                value_array = value_array + [new_value]
            value = _calculate_value(type, value_array)
        else:
            length, puzzle_input = puzzle_input[:11], puzzle_input[11:]
            value_array = []
            for _ in range(int(length, 2)):
                new_value, part_1_total, puzzle_input = _calculate_bytes(
                    puzzle_input, part_1_total)
                value_array = value_array + [new_value]
            value = _calculate_value(type, value_array)

    return (value, part_1_total, puzzle_input)


def _calculate_value(type, value_array):
    if type == "000":
        return sum(value_array)
    elif type == "001":
        return prod(value_array)
    elif type == "010":
        return min(value_array)
    elif type == "011":
        return max(value_array)
        # 4 = 100 is literal
    elif type == "101":
        return 1 if value_array[0] > value_array[1] else 0
    elif type == "110":
        return 1 if value_array[0] < value_array[1] else 0
    elif type == "111":
        return 1 if value_array[0] == value_array[1] else 0


def get_input():
    # yield from ["8A004A801A8002F478"]
    # yield from ["620080001611562C8802118E34"]
    # yield from ["C0015000016115A2E0802F182340"]
    # yield from ["A0016C880162017C3686B18A3D4780"]

    # yield from ["C200B40A82"]
    # yield from ["04005AC33890"]
    # yield from ["880086C3E88112"]
    # yield from ["CE00C43D881120"]
    # yield from ["D8005AC2A8F0"]
    # yield from ["F600BC2D8F"]
    # yield from ["9C005AC2F8F0"]
    # yield from ["9C0141080250320F1802104A08"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day16.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
