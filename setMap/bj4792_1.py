#!/usr/bin/env python
import sys
input= sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a,b = find(a),find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    blue = 0
    for c, f, t in edges:
        if find(f) == find(t):
            continue
        union(f, t)
        if c:
            blue += 1
    return blue


while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break

    edges = []
    for _ in range(m):
        c, f, t = input().split()
        f,t=int(f),int(t)
        if c == "B":
            c = 1
        else:
            c = 0
        edges.append((c, f, t))

    parent = [i for i in range(n + 1)]
    edges.sort()
    minb = kruskal()

    parent = [i for i in range(n + 1)]
    edges.sort(reverse=True)
    maxb = kruskal()

    if maxb >= k and k >= minb:
        print(1)
    else:
        print(0)

