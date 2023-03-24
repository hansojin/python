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
            print((-1)*heapq.heappop(hp))
        else:
            print(0)
    else:
        heapq.heappush(hp,m*(-1))

'''

as, heapq 모듈은
heappop(), heappush() 에 대해서 최소힙(parent<child)만 동작하기에 
max heap (parent > child) 를 구현하기 위해서 -1 을 곱해줌

'''
