#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations_with_replacement

ans=0
n=int(input())
li=list(map(int,input().split()))

if n==1:
    print(li[0])
else:
    for i in range(2,n+1):
        for c in combinations_with_replacement(li,i):
            ans+=max(c)-min(c)

print(ans%1000000007)
