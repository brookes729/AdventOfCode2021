import os.path


def day():
    puzzle_input = get_input()
    numbers_called = dict(enumerate(next(puzzle_input).split(",")))
    numbers_called_reversed = dict([(x, i)
                                    for i, x in numbers_called.items()])

    _ = next(puzzle_input)  # Ignore the second line

    best_board_win = (9999, [])
    worst_board_win = (0, [])

    while True:
        columns = [[]] * 5
        row_best = 9999
        for subline in puzzle_input:
            if subline == "":
                break

            line_numbers = list(filter(None, subline.split(" ")))

            current_row_best = max([numbers_called_reversed.get(number, 9999)
                                    for number in line_numbers])
            if current_row_best < row_best:
                row_best = current_row_best

            columns = [x + [y] for (x, y) in zip(columns, line_numbers)]

        if row_best == 9999:  # No row matched, more likely we ran out of boards
            break

        column_best = 9999
        for column in columns:
            current_column_best = max([numbers_called_reversed.get(number, "9999")
                                       for number in column])
            if current_column_best < column_best:
                column_best = current_column_best

        if min(column_best, row_best) < best_board_win[0]:
            best_board_win = (min(column_best, row_best), columns.copy())
        if min(column_best, row_best) > worst_board_win[0]:
            worst_board_win = (min(column_best, row_best), columns.copy())

    remaining_best_number_sum = sum(
        [sum([int(number) for number in column if numbers_called_reversed[number] > best_board_win[0]])
            for column in best_board_win[1]])
    remaining_worst_number_sum = sum(
        [sum([int(number) for number in column if numbers_called_reversed[number] > worst_board_win[0]])
            for column in worst_board_win[1]])

    print(
        f"Day 4 result 1 is {remaining_best_number_sum * int(numbers_called[best_board_win[0]])}")
    print(
        f"Day 4 result 2 is {remaining_worst_number_sum * int(numbers_called[worst_board_win[0]])}")


def get_input():
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day4.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
