#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
li = list(list(map(int, input().split())) for _ in range(n))
res = 10*5
hm = []
ck = []

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            hm.append([i, j])
        elif li[i][j] == 2:
            ck.append([i, j])

for c in combinations(ck, m):  
    tmp = 0            
    for h in hm:
        clen = 999  
        for j in range(m):
            clen = min(clen, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        tmp += clen
    res = min(res, tmp)
print(res)
