#!/usr/bin/env python3
# coding: utf8

import math
from itertools import count


# Value: x
# distance = range + offset
# range: n as (2n+1)^2 <= x
#     so n = int( (sqrt(x) - 1)/2 )
# offset: o = abs( n - mod(x - 1, 2n) )
def manhattan_steps_part1(value):
    n = math.ceil((math.sqrt(value) - 1)/2)

    # Special case
    if n == 0:
        return 0
    else:
        o = math.fabs(n - math.fmod(value - 1, 2 * n))
        distance = int(n + o)
        return distance


# Uses solution from https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/dqox0fv/?st=jas39005&sh=95183492
def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                         for l in range(j-1,j+2))
    for s in count(1, 2):
        for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s):   j -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): j += 1; a[i,j] = sn(i,j); yield a[i,j]


def manhattan_steps_part2(value):
    for x in sum_spiral():
        if x > value:
            return x


if __name__ == '__main__':
    print('Part1:', manhattan_steps_part1(265149))
    print('Part2:', manhattan_steps_part2(265149))
