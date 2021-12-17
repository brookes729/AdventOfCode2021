import os.path


def day():
    puzzle_input = next(get_input())
    target_x, target_y = [[int(value) for value in coord.split("=")[1].split(
        "..")] for coord in puzzle_input.split("target area: ")[1].split(",")]

    min_x, max_x = min(target_x), max(target_x)
    min_y, max_y = min(target_y), max(target_y)

    part_1_total = 0
    part_2_total = 0

    part_2_set = set()

    starting_power_x, starting_power_y = 0, 0
    increase_failed_count = 0
    highest_peak_y = 0

    while increase_failed_count < 100:  # Loop for finding best power
        power_x, power_y = starting_power_x, starting_power_y
        current_x, current_y = 0, 0
        heighest_y = 0

        while True:  # Loop for finding if it hits
            current_x, current_y = current_x + power_x, current_y + power_y
            power_x, power_y = power_x - 1 if power_x > 0 else power_x + \
                1 if power_x < 0 else power_x, power_y - 1

            if current_y > heighest_y:
                heighest_y = current_y

            if current_x > max_x:
                starting_power_x = starting_power_x - 1
                break
            if current_y < min_y:
                if current_x < min_x:
                    starting_power_x = starting_power_x + 1
                    break
                starting_power_y = starting_power_y + 1
                starting_power_x = starting_power_x - \
                    int(starting_power_x *
                        0.1)  # Reduce X power by 10% to see if we can hit this point (faster than reducing to 0)
                increase_failed_count = increase_failed_count + 1
                break
            if current_x <= max_x and current_y <= max_y and current_x >= min_x and current_y >= min_y:
                starting_power_y = starting_power_y + 1
                increase_failed_count = 0
                if heighest_y > part_1_total:
                    part_1_total = heighest_y
                    highest_peak_y = starting_power_y
                break

    # part 2 is very similar to above but over a wider range and taking into acount the max Y power for the peak
    for starting_power_x in range(max_x+1):
        for starting_power_y in range(min_y-1, highest_peak_y+1):
            power_x, power_y = starting_power_x, starting_power_y
            current_x, current_y = 0, 0
            while True:  # Loop for finding if it hits
                current_x, current_y = current_x + power_x, current_y + power_y
                power_x, power_y = power_x - 1 if power_x > 0 else power_x + \
                    1 if power_x < 0 else power_x, power_y - 1
                if current_x > max_x:
                    break
                if current_y < min_y:
                    break
                if current_x <= max_x and current_y <= max_y and current_x >= min_x and current_y >= min_y:
                    part_2_set.add((starting_power_x, starting_power_y))
                    break

    part_2_total = len(part_2_set)

    print(
        f"Day 16 result 1 is {part_1_total}")

    print(
        f"Day 16 result 2 is: {part_2_total}")


def get_input():
    # yield from ["target area: x=20..30, y=-10..-5"]
    yield from ["target area: x=34..67, y=-215..-186"]

    # try:
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../../test_inputs/day16.txt")
    #     file1 = open(path, 'r')
    #     while True:
    #         yield file1.readline().strip()
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    day()
