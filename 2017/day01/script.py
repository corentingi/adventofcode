#!/usr/bin/env python3
# coding: utf8


def sum_captcha_part1(captcha):
    result = 0
    length = len(captcha)

    # Adding the first value at the end to make it kind if circular
    captcha += captcha[0]

    for i in range(0, length):
        if captcha[i] == captcha[i+1]:
            result += int(captcha[i])

    return result


def sum_captcha_part2(captcha):
    result = 0
    length = len(captcha)

    offset = int(length/2)

    # Doubling the size to make it kind if circular
    captcha += captcha

    for i in range(0, length):
        if captcha[i] == captcha[i+offset]:
            result += int(captcha[i])

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print('Part 1:', sum_captcha_part1(input_data))
    print('Part 2:', sum_captcha_part2(input_data))
