#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]

member = list(range(n))
ans=sys.maxsize

for A in list(combinations(member,n//2)):
    start,link=0,0
    B = list(set(member)-set(A))
    for i,j in list(combinations(A,2)):
        start+=li[i][j]
        start+=li[j][i]
    for i,j in list(combinations(B,2)):
        link+=li[i][j]
        link+=li[j][i]
    ans=min(ans,abs(link-start))

print(ans)
