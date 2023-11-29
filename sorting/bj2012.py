#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
num=[i for i in range(n+1)]
li=[0]+[int(input()) for _ in range(n)]
li.sort()
ans = 0
for i in range(0,n+1):
    ans+=abs(li[i]-num[i])
print(ans)

