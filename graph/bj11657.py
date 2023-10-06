#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = 1e9

v,e=map(int,input().split())
graph = []
for _ in range(e):
    src,dst,w = map(int,input().split())
    graph.append((src,dst,w))

cost = [INF] *(v+1)

def bellman(start):
    cost[start]=0

    for i in range(v):
        for src,dst,w  in graph:
            W = cost[src]+w
            if cost[src]!=INF and cost[dst]>W:
                cost[dst] = W
                if i==v-1:
                    return False
    return True


if bellman(1):
    for i in range(2,v+1):
        tmp = cost[i]
        if tmp==INF:
            print(-1)
        else:
            print(cost[i])
else:
    print(-1)
