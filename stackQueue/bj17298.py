#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
ans=[-1 for i in range(n)]
stack=[]

for i in range(n):
    while stack and li[stack[-1]]<li[i]:
        ans[stack.pop()]=li[i]
    stack.append(i)
print(*ans)
