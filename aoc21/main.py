from days import *
from sys import modules


def main():
    dayNumber = get_day_by_input()

    while dayNumber.isnumeric() and int(dayNumber) > 0 and int(dayNumber) < 26:
        print(f"Todays day is {dayNumber}, here is the challenge")

        dayModule = modules[f"days.day{dayNumber}"]
        getattr(dayModule, f"day{dayNumber}")()

        dayNumber = get_day_by_input()

    print("Merry Christmas")


def get_day_by_input():
    print("Please enter a day for the challenge: ")
    return input()


main()
