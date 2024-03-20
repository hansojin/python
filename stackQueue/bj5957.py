#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
li=deque(i for i in range(n,0,-1))
ans,tmp=[],deque()
while len(ans)!=n:
    a,b=map(int,input().split())
    if a==1:
        for _ in range(b):
            tmp.append(li.pop())
    else:
        for _ in range(b):
            ans.append(tmp.pop())
for i in ans[::-1]:
    print(i)



