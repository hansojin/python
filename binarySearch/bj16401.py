#!/usr/bin/env python

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
li = list(map(int, input().split()))

start,end = 1,int(1e9)
res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in li:
        cnt += l // mid
    if cnt >= m:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1
print(res)
