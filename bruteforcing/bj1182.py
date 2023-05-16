#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

n,s=map(int,input().split())
li=list(map(int,input().split()))
cnt=0

for i in range(1,n+1):
    comb = combinations(li,i)

    for x in comb:
        if sum(x)==s:
            cnt+=1
print(cnt)
