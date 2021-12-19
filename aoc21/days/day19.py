import os.path


class coordinate:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

        self.neighbours = {}

    def add_neighbour(self, neighbour) -> None:
        if (self.x != neighbour.x) or (self.y != neighbour.y) or (self.y != neighbour.y):
            self.neighbours[str(neighbour)] = {"distance": (self.x - neighbour.x)**2 + (self.y - neighbour.y)**2 + (self.z - neighbour.z)**2,
                                               "dx": self.x - neighbour.x,
                                               "dy": self.y - neighbour.y,
                                               "dz": self.z - neighbour.z}

    def match(self, potential) -> bool:
        matches = len(set([potential.neighbours[potential_neighbour]["distance"] for potential_neighbour in potential.neighbours]).intersection(
            set([self.neighbours[potential_neighbour]["distance"] for potential_neighbour in self.neighbours])))

        return matches >= 11

    def rotation_match(self, potential) -> bool:
        rotation = {}
        for neighbour in self.neighbours:
            for potential_neighbour in potential.neighbours:
                if self.neighbours[neighbour]["distance"] == potential.neighbours[potential_neighbour]["distance"]:
                    if potential.neighbours[potential_neighbour]["dx"] == 0 or \
                            potential.neighbours[potential_neighbour]["dy"] == 0 or \
                            potential.neighbours[potential_neighbour]["dz"] == 0:
                        continue
                    if abs(self.neighbours[neighbour]["dx"]) == abs(potential.neighbours[potential_neighbour]["dx"]):
                        if abs(self.neighbours[neighbour]["dy"]) == abs(potential.neighbours[potential_neighbour]["dy"]):
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             1, 2, 3)
                        else:
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             1, 3, 2)
                    elif abs(self.neighbours[neighbour]["dx"]) == abs(potential.neighbours[potential_neighbour]["dy"]):
                        if abs(self.neighbours[neighbour]["dy"]) == abs(potential.neighbours[potential_neighbour]["dx"]):
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             2, 1, 3)
                        else:
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             2, 3, 1)
                    elif abs(self.neighbours[neighbour]["dx"]) == abs(potential.neighbours[potential_neighbour]["dz"]):
                        if abs(self.neighbours[neighbour]["dy"]) == abs(potential.neighbours[potential_neighbour]["dx"]):
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             2, 3, 1)
                        else:
                            test_rotation = (self.neighbours[neighbour]["dx"] /
                                             potential.neighbours[potential_neighbour]["dz"],
                                             self.neighbours[neighbour]["dy"] /
                                             potential.neighbours[potential_neighbour]["dy"],
                                             self.neighbours[neighbour]["dz"] /
                                             potential.neighbours[potential_neighbour]["dx"],
                                             3, 2, 1)
                    else:
                        continue

                    if test_rotation != rotation and (test_rotation[0]**2 == 1 and test_rotation[1]**2 == 1 and test_rotation[2]**2 == 1):
                        rotation[test_rotation] = rotation.get(
                            test_rotation, 0) + 1

        return max(rotation, key=rotation.get)

    def get_element(self, number):
        if number == 1:
            return self.x
        if number == 2:
            return self.y
        if number == 3:
            return self.z

    def __repr__(self) -> str:
        return f"{self.x},{self.y},{self.z}"


def day():
    puzzle_input = get_input()

    part_1_total = 0
    part_2_total = 0

    scanner_relative_coords = {}
    current_scanner = -1

    for line in puzzle_input:
        if line == "":
            break

        current_scanner = current_scanner + 1
        scanner_relative_coords[current_scanner] = dict()
        for coord in puzzle_input:
            if coord == "":
                break

            coord_list = coord.split(",")
            scanner_relative_coords[current_scanner][coord] = coordinate(
                coord_list[0], coord_list[1], coord_list[2])

    for scanner in scanner_relative_coords:
        for coord in scanner_relative_coords[scanner]:
            for neighbour in scanner_relative_coords[scanner]:
                scanner_relative_coords[scanner][coord].add_neighbour(
                    scanner_relative_coords[scanner][neighbour])

    scanner_coord = {0: (0, 0, 0)}

    while len(scanner_relative_coords) > 1:
        scanner_coord = {0: (0, 0, 0)}
        scanner_rotation = {0: (1, 1, 1)}
        for other_scanner in scanner_relative_coords:
            if 0 != other_scanner:
                for other_coord in scanner_relative_coords[other_scanner]:
                    for coord in scanner_relative_coords[0]:
                        if scanner_relative_coords[0][coord].match(
                                scanner_relative_coords[other_scanner][other_coord]):

                            if not other_scanner in scanner_coord:
                                rotation = scanner_relative_coords[0][coord].rotation_match(
                                    scanner_relative_coords[other_scanner][other_coord])

                                if sum(rotation) == 0:
                                    continue

                                scanner_rotation[other_scanner] = rotation

                                scanner_coord[other_scanner] = (scanner_relative_coords[0][coord].x -
                                                                (int(
                                                                    rotation[0]) * scanner_relative_coords[other_scanner][other_coord].get_element(rotation[3])),
                                                                scanner_relative_coords[0][coord].y -
                                                                (int(
                                                                    rotation[1]) * scanner_relative_coords[other_scanner][other_coord].get_element(rotation[4])),
                                                                scanner_relative_coords[0][coord].z -
                                                                (int(rotation[2]) * scanner_relative_coords[other_scanner][other_coord].get_element(rotation[5])))
                                break
                    if other_scanner in scanner_coord:
                        break

        if len(scanner_coord) > 1:
            done_list = []
            for scanner in scanner_relative_coords:
                if scanner != 0 and scanner in scanner_coord:
                    print(f"Scanner {scanner} is at {scanner_coord[scanner]}")
                    for coord in scanner_relative_coords[scanner]:
                        new_neighbour = coordinate(scanner_coord[scanner][0] + (scanner_rotation[scanner][0] * scanner_relative_coords[scanner][coord].get_element(scanner_rotation[scanner][3])),
                                                   scanner_coord[scanner][1] + (
                                                       scanner_rotation[scanner][1] * scanner_relative_coords[scanner][coord].get_element(scanner_rotation[scanner][4])),
                                                   scanner_coord[scanner][2] + (scanner_rotation[scanner][2] * scanner_relative_coords[scanner][coord].get_element(scanner_rotation[scanner][5])))

                        if str(new_neighbour) in scanner_relative_coords[0]:
                            continue

                        for zerod_coord in scanner_relative_coords[0]:
                            scanner_relative_coords[0][zerod_coord].add_neighbour(
                                new_neighbour)

                        for coord in scanner_relative_coords[0]:
                            new_neighbour.add_neighbour(
                                scanner_relative_coords[0][coord])

                        scanner_relative_coords[0][str(
                            new_neighbour)] = new_neighbour
                    done_list = done_list + [scanner]
        else:
            print("it's broke")
            break

        for scanner in done_list:
            scanner_relative_coords.pop(scanner)

    print(
        f"Day 19 result 1 is {len(scanner_relative_coords[0])}")

    print(
        f"Day 19 result 2 is: {part_2_total}")


def get_input():
    # yield from ["--- scanner 0 ---",
    #             "0,2,1",
    #             "4,1,1",
    #             "3,3,1",
    #             "",
    #             "--- scanner 1 ---",
    #             "-1,-1,1",
    #             "-5,0,1",
    #             "-2,1,1",
    #             "1,1,1"]

    # yield from ["--- scanner 0 ---",
    #             "-1,-1,1",
    #             "-2,-2,2",
    #             "-3,-3,3",
    #             "-2,-3,1",
    #             "5,6,-4",
    #             "8,0,7",
    #             "",
    #             "--- scanner 0 ---",
    #             "1,-1,1",
    #             "2,-2,2",
    #             "3,-3,3",
    #             "2,-1,3",
    #             "-5,4,-6",
    #             "-8,-7,0",
    #             "",
    #             "--- scanner 0 ---",
    #             "-1,-1,-1",
    #             "-2,-2,-2",
    #             "-3,-3,-3",
    #             "-1,-3,-2",
    #             "4,6,5",
    #             "-7,0,8",
    #             "",
    #             "--- scanner 0 ---",
    #             "1,1,-1",
    #             "2,2,-2",
    #             "3,3,-3",
    #             "1,3,-2",
    #             "-4,-6,5",
    #             "7,0,8",
    #             "",
    #             "--- scanner 0 ---",
    #             "1,1,1",
    #             "2,2,2",
    #             "3,3,3",
    #             "3,1,2",
    #             "-6,-4,-5",
    #             "0,7,-8"]

    yield from ["--- scanner 0 ---",
                "404,-588,-901",
                "528,-643,409",
                "-838,591,734",
                "390,-675,-793",
                "-537,-823,-458",
                "-485,-357,347",
                "-345,-311,381",
                "-661,-816,-575",
                "-876,649,763",
                "-618,-824,-621",
                "553,345,-567",
                "474,580,667",
                "-447,-329,318",
                "-584,868,-557",
                "544,-627,-890",
                "564,392,-477",
                "455,729,728",
                "-892,524,684",
                "-689,845,-530",
                "423,-701,434",
                "7,-33,-71",
                "630,319,-379",
                "443,580,662",
                "-789,900,-551",
                "459,-707,401",
                "",
                "--- scanner 1 ---",
                "686,422,578",
                "605,423,415",
                "515,917,-361",
                "-336,658,858",
                "95,138,22",
                "-476,619,847",
                "-340,-569,-846",
                "567,-361,727",
                "-460,603,-452",
                "669,-402,600",
                "729,430,532",
                "-500,-761,534",
                "-322,571,750",
                "-466,-666,-811",
                "-429,-592,574",
                "-355,545,-477",
                "703,-491,-529",
                "-328,-685,520",
                "413,935,-424",
                "-391,539,-444",
                "586,-435,557",
                "-364,-763,-893",
                "807,-499,-711",
                "755,-354,-619",
                "553,889,-390",
                "",
                "--- scanner 2 ---",
                "649,640,665",
                "682,-795,504",
                "-784,533,-524",
                "-644,584,-595",
                "-588,-843,648",
                "-30,6,44",
                "-674,560,763",
                "500,723,-460",
                "609,671,-379",
                "-555,-800,653",
                "-675,-892,-343",
                "697,-426,-610",
                "578,704,681",
                "493,664,-388",
                "-671,-858,530",
                "-667,343,800",
                "571,-461,-707",
                "-138,-166,112",
                "-889,563,-600",
                "646,-828,498",
                "640,759,510",
                "-630,509,768",
                "-681,-892,-333",
                "673,-379,-804",
                "-742,-814,-386",
                "577,-820,562",
                "",
                "--- scanner 3 ---",
                "-589,542,597",
                "605,-692,669",
                "-500,565,-823",
                "-660,373,557",
                "-458,-679,-417",
                "-488,449,543",
                "-626,468,-788",
                "338,-750,-386",
                "528,-832,-391",
                "562,-778,733",
                "-938,-730,414",
                "543,643,-506",
                "-524,371,-870",
                "407,773,750",
                "-104,29,83",
                "378,-903,-323",
                "-778,-728,485",
                "426,699,580",
                "-438,-605,-362",
                "-469,-447,-387",
                "509,732,623",
                "647,635,-688",
                "-868,-804,481",
                "614,-800,639",
                "595,780,-596",
                "",
                "--- scanner 4 ---",
                "727,592,562",
                "-293,-554,779",
                "441,611,-461",
                "-714,465,-776",
                "-743,427,-804",
                "-660,-479,-426",
                "832,-632,460",
                "927,-485,-438",
                "408,393,-506",
                "466,436,-512",
                "110,16,151",
                "-258,-428,682",
                "-393,719,612",
                "-211,-452,876",
                "808,-476,-593",
                "-575,615,604",
                "-485,667,467",
                "-680,325,-822",
                "-627,-443,-432",
                "872,-547,-609",
                "833,512,582",
                "807,604,487",
                "839,-516,451",
                "891,-625,532",
                "-652,-548,-490",
                "30,-46,-14"]

    # try:
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../../test_inputs/day19.txt")
    #     file1 = open(path, 'r')
    #     while True:
    #         yield file1.readline().strip()
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    day()
