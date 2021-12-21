import os.path


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    player_1_start_location = int(
        next(puzzle_input).split("starting position: ")[1])
    player_2_start_location = int(
        next(puzzle_input).split("starting position: ")[1])

    player_1_location = player_1_start_location
    player_2_location = player_2_start_location

    player_1_score = 0
    player_2_score = 0

    global dice_rolls
    dice_rolls = 0
    dice = deterministic_dice()

    while True:
        player_1_location = player_1_location + \
            next(dice) + \
            next(dice) + \
            next(dice)
        if player_1_location > 10:
            player_1_location = player_1_location % 10
            if player_1_location == 0:
                player_1_location = 10
        player_1_score = player_1_score + player_1_location

        if player_1_score >= 1000:
            break

        player_2_location = player_2_location + \
            next(dice) + \
            next(dice) + \
            next(dice)
        if player_2_location > 10:
            player_2_location = player_2_location % 10
            if player_2_location == 0:
                player_2_location = 10
        player_2_score = player_2_score + player_2_location

        if player_2_score >= 1000:
            break

    part_1_total = min(player_1_score, player_2_score) * dice_rolls

    print(
        f"Day 21 result 1 is {part_1_total}")

    global _dirac_result  # Cache resutls of calls as they will be the same if hit again
    _dirac_result = {}
    part_2_result = _dirac_dice(
        player_1_start_location, 0, player_2_start_location, 0, 1, True)
    part_2_total = max(part_2_result)

    print(
        f"Day 21 result 2 is: {part_2_total}")


def deterministic_dice():
    global dice_rolls
    while True:
        for i in range(100):
            dice_rolls = dice_rolls + 1
            yield i + 1


def _dirac_dice(player_1_location, player_1_score, player_2_location, player_2_score, occurances, is_player_1_go):
    global _dirac_result
    if (player_1_location, player_1_score, player_2_location, player_2_score, occurances, is_player_1_go) in _dirac_result:
        return _dirac_result[(player_1_location, player_1_score, player_2_location, player_2_score, occurances, is_player_1_go)]
    results = (0, 0)

    dice_probability = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    for dice_outcome in dice_probability:
        new_player_1_location, new_player_1_score, new_player_2_location, new_player_2_score = player_1_location, player_1_score, player_2_location, player_2_score
        if is_player_1_go:
            new_player_1_location = player_1_location + dice_outcome
            if new_player_1_location > 10:
                new_player_1_location = new_player_1_location % 10
                if new_player_1_location == 0:
                    new_player_1_location = 10

            new_player_1_score = player_1_score + new_player_1_location

            if new_player_1_score >= 21:
                results = (results[0] + (occurances *
                           dice_probability[dice_outcome]), results[1])
                continue
        else:
            new_player_2_location = player_2_location + dice_outcome
            if new_player_2_location > 10:
                new_player_2_location = new_player_2_location % 10
                if new_player_2_location == 0:
                    new_player_2_location = 10

            new_player_2_score = player_2_score + new_player_2_location

            if new_player_2_score >= 21:
                results = (results[0], results[1] +
                           (occurances * dice_probability[dice_outcome]))
                continue

        dirac_result = _dirac_dice(
            new_player_1_location, new_player_1_score, new_player_2_location, new_player_2_score, occurances * dice_probability[dice_outcome], not is_player_1_go)
        results = (results[0] + dirac_result[0],
                   results[1] + dirac_result[1])

    _dirac_result[(player_1_location, player_1_score, player_2_location,
                   player_2_score, occurances, is_player_1_go)] = results

    return results


def get_input():
    # yield from ["Player 1 starting position: 4",
    #             "Player 2 starting position: 8"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day21.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
