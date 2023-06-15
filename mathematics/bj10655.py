#!/usr/bin/env python

import sys
input= sys.stdin.readline
import math

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

dis = [0]
for i in range(N - 1):
    dist = abs(li[i + 1][0] - li[i][0]) + abs(li[i + 1][1] - li[i][1])
    dis.append(dist)

tot = sum(dis)

dist = 0
min_dist = math.inf
for i in range(1, N - 1):
    dist = tot - (dis[i] + dis[i + 1]) + abs(li[i + 1][0] - li[i - 1][0]) + abs(li[i + 1][1] - li[i - 1][1])
    min_dist = min(min_dist, dist)
print(min_dist)
