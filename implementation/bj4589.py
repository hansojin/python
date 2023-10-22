#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li = [list(map(int,input().split())) for _ in range(n)]
print("Gnomes:")
for i in li:
    if i==sorted(i) or i ==sorted(i,reverse=True):
        print("Ordered")
    else:
        print("Unordered")
