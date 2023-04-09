#!/usr/bin/env python

import sys
input = sys.stdin.readline
import heapq

jew=[]
bag=[]
n,k=map(int,input().split())

for _ in range(n):
    jew.append(list(map(int,input().split())))

for _ in range(k):
    bag.append(int(input()))

jew.sort()
bag.sort()

tmp=[]
ans=0

for bags in bag:
    while jew and bags>=jew[0][0]:
        heapq.heappush(tmp,-jew[0][1])
        heapq.heappop(jew)

    if tmp:
        ans+=heapq.heappop(tmp)
    elif not jew:
        break
print(-ans)
