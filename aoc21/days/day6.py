import os.path


def day():
    max_target_days = 256
    puzzle_input = [int(timer)
                    for timer in next(get_input()).split(",")]

    rainbow_fish_table = {}

    for rainbow_fish in range(1, max_target_days + 7):
        fish_count = 0
        rainbow_puzzle_input = [rainbow_fish]

        while len(rainbow_puzzle_input) > 0:
            fish_timer, rainbow_puzzle_input = rainbow_puzzle_input[0], rainbow_puzzle_input[1:]

            if fish_timer in rainbow_fish_table:
                fish_count = fish_count + rainbow_fish_table[fish_timer]
                continue

            for week_timer in range(1, int(fish_timer / 7) + 1):
                next_fish_timer = fish_timer - (week_timer * 7)

                if next_fish_timer > 2:
                    rainbow_puzzle_input = rainbow_puzzle_input + \
                        [next_fish_timer - 2]
                elif next_fish_timer > 0:
                    fish_count = fish_count + 1
            fish_count = fish_count + 1

        rainbow_fish_table[rainbow_fish] = fish_count

    print(
        f"Day 6 result 1 is {sum([rainbow_fish_table[80 + 7 - fish] for fish in puzzle_input])}")
    print(
        f"Day 6 result 2 is {sum([rainbow_fish_table[256 + 7 - fish] for fish in puzzle_input])}")


def get_input():
    # yield "3,4,3,1,2"
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day6.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
