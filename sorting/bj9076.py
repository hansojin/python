#!/usr/bin/env python

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    li=list(map(int,input().split()))
    li.sort()
    if li[3]-li[1]<4:
        print(sum(li[1:4]))
    else:
        print('KIN')
