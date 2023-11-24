#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = int(1e9)

graph= [[INF]*(26) for _ in range(26)]
for i in range(26):
    graph[i][i]=0
for _ in range(int(input())):
    start,end=input().rstrip().split(" is ")
    start,end=ord(start)-97,ord(end)-97
    graph[start][end]=1

for k in range(26):
    for a in range(26):
        for b in range(26):
            graph[a][b]= min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(int(input())):
    start,end=input().rstrip().split(" is ")
    start,end=ord(start)-97,ord(end)-97
    if graph[start][end]==INF:
        print("F")
    else:
        print("T")

