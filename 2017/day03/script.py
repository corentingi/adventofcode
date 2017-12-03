#!/usr/bin/env python3
# coding: utf8

import math


# Value: x
# distance = range + offset
# range: n as (2n+1)^2 <= x
#     so n = int( (sqrt(x) - 1)/2 )
# offset: o = abs( n - mod(x - 1, 2n) )
def manhattan_steps(value):
    n = math.ceil((math.sqrt(value) - 1)/2)

    # Special case
    if n == 0:
        return 0
    else:
        o = math.fabs(n - math.fmod(value - 1, 2 * n))
        distance = int(n + o)
        return distance


if __name__ == '__main__':
    print(manhattan_steps(265149))
