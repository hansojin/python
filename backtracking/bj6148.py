#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

li=[]
n,b=map(int,input().split())
for _ in range(n):
    li.append(int(input()))

minn=1e9
for i in range(1,n+1):
    comb = list(combinations(li,i))
    for j in comb:
        summ=sum(j)
        if summ>=b:
            minn=min(minn,summ)
print(minn-b)
