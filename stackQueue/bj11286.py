#!/usr/bin/env python

import heapq
import sys
input = sys.stdin.readline

hp=[]

n=int(input())
for i in range(n):
    m=int(input())
    
    if m==0:
        if hp:
            print(heapq.heappop(hp)[1])
        else:
            print(0)
    else:
        heapq.heappush(hp,(abs(m),m))
