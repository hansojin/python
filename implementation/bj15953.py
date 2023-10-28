#!/usr/bin/env python

t = int(input())

def f1(sc):
    if sc == 1:
        return 5000000
    elif 1 < sc <= 3:
        return 3000000
    elif 3 < sc <= 6:
        return 2000000
    elif 6 < sc <= 10:
        return 500000
    elif 10 < sc <= 15:
        return 300000
    elif 15 < sc <= 21:
        return 100000
    else:
        return 0
def f2(sc):
    if sc == 1:
        return 5120000
    elif 1 < sc <= 3:
        return 2560000
    elif 3 < sc <= 7:
        return 1280000
    elif 7 < sc <= 15:
        return 640000
    elif 15 < sc <= 31:
        return 320000
    else:
        return 0
for _ in range(t):
    first, second = map(int, input().split(' '))
    print(f1(first) + f2(second))
