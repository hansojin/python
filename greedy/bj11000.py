#!/usr/bin/env python

import heapq
import sys

n = int(input())

'''
q = []
for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])
q.sort()
 # 해당 코드 시간 초과
 # 아래 처럼 작성 하자
'''
q=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q.sort(key=lambda a:a[0])

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 지금 end 보다 nxt srt가 빠르면
        heapq.heappush(room, q[i][1]) # new room 개설
    else: # 그대로 유지
        heapq.heappop(room) # 근데 지금 시간은 pop,  새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))
