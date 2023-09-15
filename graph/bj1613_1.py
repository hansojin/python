#!/usr/bin/env python

import sys
input= sys.stdin.readline

def fs():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):    
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

n, k = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
fs()

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)

