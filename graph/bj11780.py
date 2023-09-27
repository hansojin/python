#!/usr/bin/env python

import sys
input= sys.stdin.readline
import math

n = int(input())
m = int(input())
path = [[[] for _ in range(n+1)] for _ in range(n+1)]
dist = [[math.inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
	a, b, c = map(int,input().split())
	dist[a][b] = min(dist[a][b], c)
	path[a][b] = [a, b]

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i != j:
				if dist[i][j] > dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
					path[i][j] = path[i][k][:-1] + path[k][j]

for i in dist[1:]:
	for j in i[1:]:
		print(0 if j == math.inf else j, end = ' ')
	print()
for i in range(1, n+1):
	for j in range(1, n+1):
		if dist[i][j] == math.inf or i == j:
			print(0)
		else:
			print(len(path[i][j]), *path[i][j])
