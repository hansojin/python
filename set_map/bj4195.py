#!/usr/bin/env python

import sys
input= sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        p[b] = a
        nb[a] += nb[b]
    print(nb[a])


for _ in range(int(input())):
    num = int(input())
    p, nb = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in p:
            p[a] = a
            nb[a] = 1
        if b not in p:
            p[b] =b
            nb[b] = 1
        union(a, b)
