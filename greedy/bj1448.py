#!/usr/bin/env python

import sys
input= sys.stdin.readline
li=[]
ans=-1
n=int(input())
for _ in range(n):
    li.append(int(input()))
li.sort(reverse=True)
for i in range(n - 2):
    if li[i] < li[i + 1] + li[i + 2]:
        ans = li[i] + li[i + 1] + li[i + 2]
        break
print(ans)
