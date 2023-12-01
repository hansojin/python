#!/usr/bin/env python

parent,level,idx,edge,conf=[],[],[],[],[]

def find(u):
    while u != parent[u]:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if level[u] > level[v]:
        u, v = v, u
    parent[u] = v
    if level[u] == level[v]:
        level[v] += 1


n=int(input())
m=int(input())
idx = [-1] * (n + 1)
parent = list(range(n + 1))
level = [0] * (n + 1)
edge = [[101] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    edge[i][i] = 0

for _ in range(m):
    s, e = map(int, input().split())
    union(s, e)
    edge[s][e] = edge[e][s] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if edge[j][k] > edge[j][i] + edge[i][k]:
                edge[j][k] = edge[j][i] + edge[i][k]

for i in range(1, n + 1):
    s = 0
    f = find(i)
    for j in range(1, n + 1):
        s = max(s, 0 if edge[i][j] == 101 else edge[i][j])
    if idx[f] != -1:
        if conf[idx[f]][1] > s:
            conf[idx[f]] = (i, s)
    else:
        idx[f] = len(conf)
        conf.append((i, s))

conf.sort()
print(len(conf))
for c in conf:
    print(c[0])

