import os.path


def day():
    forward = 0
    depth = 0
    aim = 0
    real_depth = 0

    for instruction in get_input():
        if instruction == "":
            break

        direction, distance = instruction.split(" ")
        distance = int(distance)

        match direction:
            case "forward":
                forward = forward + distance
                real_depth = real_depth + (distance * aim)
            case "down":
                depth = depth + distance
                aim = aim + distance
            case "up":
                depth = depth - distance
                aim = aim - distance

    print(f"Day 2 result 1 is {forward * depth}")
    print(f"Day 2 result 2 is {forward * real_depth}")


def get_input():
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day2.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
