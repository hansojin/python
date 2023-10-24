#!/usr/bin/env python

import sys
input= sys.stdin.readline
import bisect

n=int(input())
li=list(map(int,input().split()))

#dp = [1]*n
#for i in range(1,n):
#    for j in range(0,i):
#        if li[j]<li[i]:
#            dp[i]=max(dp[i],dp[j]+1)
#print(dp[-1])

stack=[0]

for i in li:
    if stack[-1]<i:
        stack.append(i)
    else:
        stack[bisect.bisect_left(stack,i)]=i
print(len(stack)-1)
