#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
stack=[]
s=0

for i in range(n):
    val=int(input())
    start=i
    while stack and stack[-1][1]>=val:
        start,pre=stack.pop()
        s=max(s,(i-start)*pre)
    stack.append([start,val])

while stack:
    start,pre=stack.pop()
    s=max(s,(n-start)*pre)
print(s)
