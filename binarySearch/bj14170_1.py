#!/usr/bin/env python

import sys
input= sys.stdin.readline
from bisect import bisect_left, bisect_right

def pos(start, end, li):
    left, right = 0, len(li) - 1
    sp = bisect_left(li, start)
    ep = bisect_right(li, end)

    count = ep - sp

    return count


n, q = map(int, input().split())
li = sorted(list(map(int, input().split())))

for _ in range(q):
    s, e = map(int, input().split())
    result = pos(s, e, li)
    print(result)

