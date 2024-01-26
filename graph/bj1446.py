#!/usr/bin/env python

import sys
input= sys.stdin.readline

n, d = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
graph = [i for i in range(d+1)]

for i in range(d+1):
	graph[i] = min(graph[i],graph[i-1]+1)
	for srt,end,leng in li:
		if i == srt and end <= d:
			graph[end] = min(graph[end],graph[i]+leng)

print(graph[-1])
