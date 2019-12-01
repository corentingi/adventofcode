#!/usr/bin/env python3
# coding: utf8


import math
import re



def fuel_required(mass):
    return math.floor(int(mass) / 3.) - 2


def total_fuel_required(mass):
    fuel = fuel_required(mass)

    if fuel > 0:
        return fuel + total_fuel_required(fuel)
    else:
        return 0


def module_mass_part1(input_data):
    lines = re.split('\n', input_data.strip())
    masses = [fuel_required(line) for line in lines]
    return sum(masses)


def module_mass_part2(input_data):
    lines = re.split('\n', input_data.strip())
    masses = [total_fuel_required(line) for line in lines]
    return sum(masses)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print('Part 1:', module_mass_part1(input_data))
    print('Part 2:', module_mass_part2(input_data))
