import random
import time
import itertools
import sys
import math

if len(sys.argv) != 3:
    print("Arguments not provided")
    sys.exit(-1)

instruction = sys.argv[1]
inputString = sys.argv[2]
random.seed(time.perf_counter_ns())


def roll_die(die_size):
    rd_roll = random.randrange(1, die_size)
    # print("Roll: " + str(rd_roll) + " from " + str(die_size))
    return rd_roll


def roll_set(die_number, die_size):
    rs_rolls = []
    for useless_variable in range(die_number):
        rs_roll = roll_die(die_size)
        rs_rolls.append(rs_roll)

    return rs_rolls


def sum_list(value_list):
    value_sum = 0
    for sl_value in value_list:
        value_sum += sl_value

    return value_sum


components = inputString.split("+")

dice = []
static = 0
rolls = []
result = 0

for component in components:
    if "d" in component:
        dice.append(component)
    else:
        static += int(component)

if instruction == "--stats" or instruction == "-s" or instruction == "--all" or instruction == "-a":
    die_ranges = []
    for die in dice:
        [number, size] = die.split("d")
        for i in range(int(number)):
            die_ranges.append([*range(1, int(size) + 1)])
    permutations = list(itertools.product(*die_ranges))

    stats = {}
    for j in range(sum_list(permutations[-1]) + static + 1):
        stats[j] = 0

    for perm in permutations:
        perm_sum = static
        for value in perm:
            perm_sum += value
        stats[sum_list(perm) + static] += 1

    for stat in stats.keys():
        if stats[stat] != 0:
            print_string = ""
            print_string += str(stat) + ": "
            if stat < 10:
                print_string += " "
            for count in range(stats[stat]):
                print_string += "|"
            print(print_string)

if instruction == "--roll" or instruction == "-r" or instruction == "--all" or instruction == "-a":
    for die in dice:
        [number, size] = die.split("d")

        die_rolls = roll_set(int(number), int(size))
        for roll in die_rolls:
            rolls.append(roll)
    for roll in rolls:
        result += roll

    result += static

    # print(rolls)
    print(inputString + ": " + str(result))

if instruction == "--all" or instruction == "-a":
    stat_sum = 0
    for stat in stats:
        stat_sum += stat
    print(rolls)
    print(str(math.floor((stats[result] / stat_sum) * 100)) + "% chance")




