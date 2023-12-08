#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(a, parent):
    if parent[a] == a:
        return a
    else:
        return find(parent[a], parent)

def union(a, b, parent, ranks):
    if a > b:
        a, b = b, a
    a = find(a, parent)
    b = find(b, parent)
    if a == b:
        return True
    if ranks[a] == ranks[b]:
        ranks[a] += 1
        parent[b] = a
    elif ranks[a] > ranks[b]:
        parent[b] = a
    elif ranks[b] > ranks[a]:
        parent[a] = b
    return False

for _ in range(int(input())):
    n=int(input())
    m=int(input())
    graph = False

    if m != n - 1:
        print("graph")
        for _ in range(m):
            input()
        continue

    parent = list(range(n))
    ranks = [1] * n

    for _ in range(m):
        u, v = map(int, input().split())
        if union(u - 1, v - 1, parent, ranks):
            print("graph")
            graph = True
            break

    if not graph:
        print("tree")

