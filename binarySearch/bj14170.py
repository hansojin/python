#!/usr/bin/env python

import sys
input= sys.stdin.readline

def bsleft(li, x):
    left, right = 0, len(li)

    while left < right:
        mid = (left + right) // 2
        if li[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left

def bsright(li, x):
    left, right = 0, len(li)

    while left < right:
        mid = (left + right) // 2
        if li[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


n, q = map(int, input().split())
li = sorted(list(map(int, input().split())))

for _ in range(q):
    s, e = map(int, input().split())
    sp = bsleft(li, s)
    ep = bsright(li, e)
    print(ep-sp)

