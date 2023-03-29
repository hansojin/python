#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
ans=[]
for i in range(0,n):
    for j in range(i+1,n):
        if li[j]>li[i]:
            ans.append(li[j])
            break
    else:
        ans.append(-1)
print(*ans)
