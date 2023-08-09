#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

n=int(input())
left = []
right = []

for _ in range(n):
    x=int(input())

    if len(left) == len(right):
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)

    if left and right and left[0]*-1 > right[0]:
        maxx = heapq.heappop(left)
        minn = heapq.heappop(right)

        heapq.heappush(left, minn*-1)
        heapq.heappush(right,maxx*-1)
    print(left[0]*-1)

