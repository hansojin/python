#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[input() for _ in range(int(input()))]

if li==sorted(li):
    print("INCREASING")
elif li==sorted(li,reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
