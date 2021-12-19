import os.path


class grid:
    def __init__(self) -> None:
        self.grid = set()
        self._rotated = dict()

    def add_beacon(self, coord) -> None:
        self.grid.add(coord)

    def rotate(self, rotation_number):
        if rotation_number in self._rotated:
            return self._rotated[rotation_number]
        output = set()
        for beacon in self.grid:
            if rotation_number == 0:
                output.add(beacon)
            elif rotation_number == 1:
                output.add((beacon[1], beacon[2], beacon[0]))
            elif rotation_number == 2:
                output.add((beacon[2], beacon[0], beacon[1]))
            elif rotation_number == 3:
                output.add((-beacon[0], beacon[2], beacon[1]))
            elif rotation_number == 4:
                output.add((beacon[2], beacon[1], -beacon[0]))
            elif rotation_number == 5:
                output.add((beacon[1], -beacon[0], beacon[2]))
            elif rotation_number == 6:
                output.add((beacon[0], beacon[2], -beacon[1]))
            elif rotation_number == 7:
                output.add((beacon[2], -beacon[1], beacon[0]))
            elif rotation_number == 8:
                output.add((-beacon[1], beacon[0], beacon[2]))
            elif rotation_number == 9:
                output.add((beacon[0], -beacon[2], beacon[1]))
            elif rotation_number == 10:
                output.add((-beacon[2], beacon[1], beacon[0]))
            elif rotation_number == 11:
                output.add((beacon[1], beacon[0], -beacon[2]))
            elif rotation_number == 12:
                output.add((-beacon[0], -beacon[1], beacon[2]))
            elif rotation_number == 13:
                output.add((-beacon[1], beacon[2], -beacon[0]))
            elif rotation_number == 14:
                output.add((beacon[2], -beacon[0], -beacon[1]))
            elif rotation_number == 15:
                output.add((-beacon[0], beacon[1], -beacon[2]))
            elif rotation_number == 16:
                output.add((beacon[1], -beacon[2], -beacon[0]))
            elif rotation_number == 17:
                output.add((-beacon[2], -beacon[0], beacon[1]))
            elif rotation_number == 18:
                output.add((beacon[0], -beacon[1], -beacon[2]))
            elif rotation_number == 19:
                output.add((-beacon[1], -beacon[2], beacon[0]))
            elif rotation_number == 20:
                output.add((-beacon[2], beacon[0], -beacon[1]))
            elif rotation_number == 21:
                output.add((-beacon[0], -beacon[2], -beacon[1]))
            elif rotation_number == 22:
                output.add((-beacon[2], -beacon[1], -beacon[0]))
            elif rotation_number == 23:
                output.add((-beacon[1], -beacon[0], -beacon[2]))

        self._rotated[rotation_number] = output

        return output


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    scanner_relative_grid = {}
    current_scanner = -1

    for line in puzzle_input:
        if line == "":
            break

        current_scanner = current_scanner + 1
        scanner_relative_grid[current_scanner] = grid()
        for coord in puzzle_input:
            if coord == "":
                break

            coord_list = coord.split(",")
            scanner_relative_grid[current_scanner].add_beacon(
                (int(coord_list[0]), int(coord_list[1]), int(coord_list[2])))

    known_locations = scanner_relative_grid.pop(0)
    known_scanners = {0: (0, 0, 0, 0)}

    while len(scanner_relative_grid) + 1 != len(known_scanners):
        for grid_number in scanner_relative_grid:
            if grid_number in known_scanners:
                continue
            for rotation in range(24):
                if grid_number in known_scanners:
                    break
                print(f"Trying {grid_number} - Rotation {rotation}")
                rotated_set = scanner_relative_grid[grid_number].rotate(
                    rotation)
                for test_beacon in rotated_set:
                    if grid_number in known_scanners:
                        break
                    known_beacon_list = set(known_locations.grid)
                    for known_beacon in known_beacon_list:
                        if grid_number in known_scanners:
                            break
                        test_scanner = (known_beacon[0] - test_beacon[0],
                                        known_beacon[1] - test_beacon[1],
                                        known_beacon[2] - test_beacon[2])

                        matched_beacons = 0
                        rotated_list = list(rotated_set)
                        while True:
                            rotated_beacon, rotated_list = rotated_list[0], rotated_list[1:]
                            if (test_scanner[0] + rotated_beacon[0],
                                test_scanner[1] + rotated_beacon[1],
                                    test_scanner[2] + rotated_beacon[2]) in known_locations.grid:
                                matched_beacons = matched_beacons + 1
                            if matched_beacons == 12:
                                for beacon in rotated_set:
                                    known_locations.add_beacon((test_scanner[0] + beacon[0],
                                                                test_scanner[1] +
                                                                beacon[1],
                                                                test_scanner[2] + beacon[2]))
                                known_scanners[grid_number] = (
                                    test_scanner[0], test_scanner[1], test_scanner[2], rotation)
                                break
                            if matched_beacons + len(rotated_list) < 12:
                                break

    print(
        f"Day 19 result 1 is {len(known_locations.grid)}")

    part_2_total = max([sum(map(abs, (known_scanners[i][0] - known_scanners[j][0],
                                      known_scanners[i][1] -
                                      known_scanners[j][1],
                                      known_scanners[i][2] - known_scanners[j][2]))) for i in known_scanners for j in known_scanners])

    print(
        f"Day 19 result 2 is: {part_2_total}")


def get_input():
    # yield from ["--- scanner 0 ---",
    #             "0,2,1",
    #             "4,1,2",
    #             "3,3,3",
    #             "",
    #             "--- scanner 1 ---",
    #             "-1,-1,2",
    #             "-5,0,1",
    #             "-2,1,3",
    #             "1,1,1"]

    # yield from ["--- scanner 0 ---",
    #             "404,-588,-901",
    #             "528,-643,409",
    #             "-838,591,734",
    #             "390,-675,-793",
    #             "-537,-823,-458",
    #             "-485,-357,347",
    #             "-345,-311,381",
    #             "-661,-816,-575",
    #             "-876,649,763",
    #             "-618,-824,-621",
    #             "553,345,-567",
    #             "474,580,667",
    #             "-447,-329,318",
    #             "-584,868,-557",
    #             "544,-627,-890",
    #             "564,392,-477",
    #             "455,729,728",
    #             "-892,524,684",
    #             "-689,845,-530",
    #             "423,-701,434",
    #             "7,-33,-71",
    #             "630,319,-379",
    #             "443,580,662",
    #             "-789,900,-551",
    #             "459,-707,401",
    #             "",
    #             "--- scanner 1 ---",
    #             "686,422,578",
    #             "605,423,415",
    #             "515,917,-361",
    #             "-336,658,858",
    #             "95,138,22",
    #             "-476,619,847",
    #             "-340,-569,-846",
    #             "567,-361,727",
    #             "-460,603,-452",
    #             "669,-402,600",
    #             "729,430,532",
    #             "-500,-761,534",
    #             "-322,571,750",
    #             "-466,-666,-811",
    #             "-429,-592,574",
    #             "-355,545,-477",
    #             "703,-491,-529",
    #             "-328,-685,520",
    #             "413,935,-424",
    #             "-391,539,-444",
    #             "586,-435,557",
    #             "-364,-763,-893",
    #             "807,-499,-711",
    #             "755,-354,-619",
    #             "553,889,-390",
    #             "",
    #             "--- scanner 2 ---",
    #             "649,640,665",
    #             "682,-795,504",
    #             "-784,533,-524",
    #             "-644,584,-595",
    #             "-588,-843,648",
    #             "-30,6,44",
    #             "-674,560,763",
    #             "500,723,-460",
    #             "609,671,-379",
    #             "-555,-800,653",
    #             "-675,-892,-343",
    #             "697,-426,-610",
    #             "578,704,681",
    #             "493,664,-388",
    #             "-671,-858,530",
    #             "-667,343,800",
    #             "571,-461,-707",
    #             "-138,-166,112",
    #             "-889,563,-600",
    #             "646,-828,498",
    #             "640,759,510",
    #             "-630,509,768",
    #             "-681,-892,-333",
    #             "673,-379,-804",
    #             "-742,-814,-386",
    #             "577,-820,562",
    #             "",
    #             "--- scanner 3 ---",
    #             "-589,542,597",
    #             "605,-692,669",
    #             "-500,565,-823",
    #             "-660,373,557",
    #             "-458,-679,-417",
    #             "-488,449,543",
    #             "-626,468,-788",
    #             "338,-750,-386",
    #             "528,-832,-391",
    #             "562,-778,733",
    #             "-938,-730,414",
    #             "543,643,-506",
    #             "-524,371,-870",
    #             "407,773,750",
    #             "-104,29,83",
    #             "378,-903,-323",
    #             "-778,-728,485",
    #             "426,699,580",
    #             "-438,-605,-362",
    #             "-469,-447,-387",
    #             "509,732,623",
    #             "647,635,-688",
    #             "-868,-804,481",
    #             "614,-800,639",
    #             "595,780,-596",
    #             "",
    #             "--- scanner 4 ---",
    #             "727,592,562",
    #             "-293,-554,779",
    #             "441,611,-461",
    #             "-714,465,-776",
    #             "-743,427,-804",
    #             "-660,-479,-426",
    #             "832,-632,460",
    #             "927,-485,-438",
    #             "408,393,-506",
    #             "466,436,-512",
    #             "110,16,151",
    #             "-258,-428,682",
    #             "-393,719,612",
    #             "-211,-452,876",
    #             "808,-476,-593",
    #             "-575,615,604",
    #             "-485,667,467",
    #             "-680,325,-822",
    #             "-627,-443,-432",
    #             "872,-547,-609",
    #             "833,512,582",
    #             "807,604,487",
    #             "839,-516,451",
    #             "891,-625,532",
    #             "-652,-548,-490",
    #             "30,-46,-14"]

    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../../test_inputs/day19.txt")
        file1 = open(path, 'r')
        while True:
            yield file1.readline().strip()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    day()
