#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq

for _ in range(int(input())):
    k=int(input())
    visit=[0]*k
    maxh,minh=[],[]

    for i in range(k):
        op,n=input().split()
        n=int(n)

        if op=='I':
            heapq.heappush(maxh,(-n,i))
            heapq.heappush(minh,(n,i))
            visit[i]=1
        elif n==1:
            while minh and not visit[maxh[0][1]]:
                heapq.heappop(maxh)
            if maxh:
                visit[maxh[0][1]]=0
                heapq.heappop(maxh)
        else:
            while minh and not visit[minh[0][1]]:
                heapq.heappop(minh)
            if minh:
                visit[minh[0][1]]=0
                heapq.heappop(minh)
        while minh and not visit[minh[0][1]]:
            heapq.heappop(minh)
        while maxh and not visit[maxh[0][1]]:
            heapq.heappop(maxh)
    if maxh and minh:
        print(-maxh[0][0], minh[0][0])
    else:
        print("EMPTY")
