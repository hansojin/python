#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input().rstrip())):
    l, r = 1, 1e9

    n = int(input().rstrip())
    exp = n*(n+1) // 2

    while l<=r:
        mid = (l+r) // 2
        if mid * (mid+1) <= exp:
            l = mid+ 1
        else:
            r = mid- 1
    print(int(l))
