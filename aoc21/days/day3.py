import os.path


def day():
    line_length = len(next(get_input()))
    count_of_ones = [0] * line_length
    line_count = 0
    columns = [[]] * line_length

    for line in get_input():
        if line == "":
            break

        line_count = line_count + 1
        new_count_of_ones = [int(char) for char in line if char.isnumeric()]

        count_of_ones = [
            x + y for (x, y) in zip(new_count_of_ones, count_of_ones)]

        columns = [
            x + [y] for (x, y) in zip(columns, new_count_of_ones)]

    dominant_number = [(count >
                        (line_count / 2)) for count in count_of_ones]
    gamma = int(
        '0b' + ''.join(['1' if x else '0' for x in dominant_number]), 2)
    epsilon = int(
        '0b' + ''.join(['0' if x else '1' for x in dominant_number]), 2)

    global remaining_oxygen_potential, remaining_carbon_potential
    remaining_oxygen_potential = [index for index in range(
        len(columns[0])) if columns[0][index] == int(dominant_number[0])]
    remaining_carbon_potential = [index for index in range(
        len(columns[0])) if columns[0][index] != int(dominant_number[0])]

    for column_index in range(1, line_length-1):
        next_dominant_oxygen_value = int(sum([columns[column_index][index] for index in remaining_oxygen_potential]) >= (
            len([columns[column_index][index] for index in remaining_oxygen_potential]) / 2))
        next_dominant_carbon_value = int(sum([columns[column_index][index] for index in remaining_carbon_potential]) >= (
            len([columns[column_index][index] for index in remaining_carbon_potential]) / 2))

        if len(remaining_oxygen_potential) > 1:
            remaining_oxygen_potential = [
                index for index in remaining_oxygen_potential if columns[column_index][index] == next_dominant_oxygen_value]

        if len(remaining_carbon_potential) > 1:
            remaining_carbon_potential = [
                index for index in remaining_carbon_potential if columns[column_index][index] != next_dominant_carbon_value]

    oxygen = int(
        '0b' + ''.join([str(columns[column_index][remaining_oxygen_potential[0]]) for column_index in range(line_length-1)]), 2)
    carbon = int(
        '0b' + ''.join([str(columns[column_index][remaining_carbon_potential[0]]) for column_index in range(line_length-1)]), 2)

    print(f"Day 3 result 1 is {gamma * epsilon}")
    print(f"Day 3 result 2 is {oxygen *  carbon}")


def get_input():
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day3.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
