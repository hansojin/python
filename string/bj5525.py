#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())
s=list(input())
ans,cnt=0,0
stack=[]

for i in range(m):
    if s[i]=='I':
        stack.append(i)

for i in range(1,len(stack)):
    if stack[i]-stack[i-1]==2:
        cnt+=1
    else:
        cnt=0
    if cnt>=n:
        ans+=1
print(ans)
