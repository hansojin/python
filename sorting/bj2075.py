#!/usr/bin/env python

import sys
input = sys.stdin.readline
import heapq

heap=[]
n=int(input())

for i in range(n):
    nums=list(map(int,input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap,num)
    else:
        for num in nums:
            if heap[0]<num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
print(heap[0])
