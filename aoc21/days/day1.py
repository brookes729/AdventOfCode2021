import os.path


def day1():
    last_depth = 99999
    second_last = 0
    third_last = 0
    last_rolling_depth = 999999
    depth_increased = 0
    depth_increased_rolling = 0

    for depth in get_input():
        if depth == "":
            break

        depth = int(depth)

        if depth > last_depth:
            depth_increased = depth_increased + 1

        if third_last != 0:
            if depth + last_depth + second_last > last_rolling_depth:
                depth_increased_rolling = depth_increased_rolling + 1

            last_rolling_depth = depth + last_depth + second_last

        last_depth, second_last, third_last = depth, last_depth, second_last

    print(f"Day one part one solution is {depth_increased}")
    print(f"Day one part two solution is {depth_increased_rolling}")


def get_input():
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day1.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day1()
