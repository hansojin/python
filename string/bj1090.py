#!/usr/bin/env python

import sys
input= sys.stdin.readline

maxx=0

for _ in range(int(input())):
    score=0
    point = list(map(int,input().split()))
    score+=max(point[0],point[1])
    point = point[2:]
    point.sort(reverse=True)
    score+=sum(point[0:2])
    maxx=max(maxx,score)
print(maxx)
