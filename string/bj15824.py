#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

n=int(input())
li=list(map(int,input().split()))
tmp=[]
if n==1:
    print(li[0])
else:
    for i in range(2,n+1):
        sc=combinations(li,i)
        tmp.extend(sc)
ans=0
for i in tmp:
    ans+=max(i)-min(i)
print(ans%1000000007)


