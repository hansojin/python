#!/usr/bin/env python

import sys
input= sys.stdin.readline

N, M = map(int, input().rstrip().split())

dic = {}
for _ in range(N):
    group = input().rstrip()
    mem = []
    num = int(input())
    for _ in range(num):
        name = input().rstrip()
        dic[name] = group
        mem.append(name)
    mem.sort()
    dic[group] = mem
for _ in range(M):
    name = input().rstrip()
    n = int(input())
    if n == 1:
        print(dic[name])
    else:
        for member in dic[name]:
            print(member)
