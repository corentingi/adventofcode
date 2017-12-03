#!/usr/bin/env python3
# coding: utf8


def sum_captcha(captcha):
    result = 0
    length = len(captcha)
    captcha += captcha[0]

    for i in range(0, length):
        if captcha[i] == captcha[i+1]:
            result += int(captcha[i])

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = str(f.read()).strip()

    print(sum_captcha(input_data))
