import os.path


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    enhancement = dict(enumerate(next(puzzle_input)))
    next(puzzle_input)

    image = {}
    row = 0

    for line in puzzle_input:
        if line == "":
            break

        for index, pixel in enumerate(line):
            image[(row, index)] = pixel == "#"
        row = row + 1

    default_pixel = False
    #_visualise_image(image, default_pixel)

    for step in range(2):
        print(f"Step {step}")
        image = _enhance(image, enhancement, default_pixel)
        default_pixel = enhancement[0] == "#" if default_pixel == False else enhancement[511] == "#"
        #_visualise_image(image, default_pixel)

    part_1_total = len([image[i] for i in image if image[i] == True])

    for step in range(48):
        print(f"Step {step + 2}")
        image = _enhance(image, enhancement, default_pixel)
        default_pixel = enhancement[0] == "#" if default_pixel == False else enhancement[511] == "#"
        #_visualise_image(image, default_pixel)

    part_2_total = len([image[i] for i in image if image[i] == True])

    print(
        f"Day 20 result 1 is {part_1_total}")

    print(
        f"Day 20 result 2 is: {part_2_total}")


def _enhance(image, enhancement, default_pixel):
    new_image = {}
    x_max, y_max = max([dot[0] for dot in image]), max(
        [dot[1] for dot in image])
    x_min, y_min = min([dot[0] for dot in image]), min(
        [dot[1] for dot in image])

    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            new_value = 0
            power_of_two = 8
            for neighbour in [(-1, -1), (-1, 0), (-1, 1),
                              (0, -1), (0, 0), (0, 1),
                              (1, -1), (1, 0), (1, 1)]:
                new_value = new_value + \
                    (2**power_of_two if image.get((x +
                     neighbour[0], y+neighbour[1]), default_pixel) else 0)
                power_of_two = power_of_two - 1
            new_image[(x, y)] = enhancement[new_value] == "#"

    return new_image


def _visualise_image(image, default_pixel):
    x_max, y_max = max([dot[0] for dot in image]), max(
        [dot[1] for dot in image])
    x_min, y_min = min([dot[0] for dot in image]), min(
        [dot[1] for dot in image])

    for x in range(x_min - 1, x_max + 2):
        line = ""
        for y in range(y_min - 1, y_max + 2):
            if image.get((x, y), default_pixel):
                line = line + "#"
            else:
                line = line + "."
        print(line)


def get_input():
    # yield from ["..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##" +
    #             "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###" +
    #             ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#." +
    #             ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....." +
    #             ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.." +
    #             "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....." +
    #             "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
    #             "",
    #             "#..#.",
    #             "#....",
    #             "##..#",
    #             "..#..",
    #             "..###"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day20.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
