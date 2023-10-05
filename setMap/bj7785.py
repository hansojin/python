#!/usr/bin/env python

import sys
input = sys.stdin.readline
li={}
n=int(input())
for _ in range(n):
    a,b=input().split()
    if b=='enter':
        li[a]=b
    if b=='leave':
        del li[a]

for i in sorted(li,reverse=True):
    print(i)
