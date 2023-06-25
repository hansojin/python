#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

n=int(input())
card=[]

for _ in range(n):
    heapq.heappush(card,int(input()))
if len(card)==1:
    print(0)
else:
    ans=0
    while len(card)>1:
        tmp1=heapq.heappop(card)
        tmp2=heapq.heappop(card)
        ans+=(tmp1+tmp2)
        heapq.heappush(card,tmp1+tmp2)
    print(ans)
