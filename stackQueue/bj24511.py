#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
da = list(map(int,input().split()))
db = list(map(int,input().split()))
m=int(input())
dc= list(map(int,input().split()))
ans=deque()

for qs in range(n):
    if da[qs]==0:
        ans.appendleft(db[qs])
for i in range(m):
    ans.append(dc[i])
    print(ans.popleft(),end=' ')


