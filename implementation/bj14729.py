#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[float(input()) for _ in range(int(input()))]

li.sort()
for i in range(7):
    print('{:.3f}'.format(li[i]))
