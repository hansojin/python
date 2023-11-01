#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
s=sum(li)
ans=0
for num in li:
    s-=num
    ans+=num*s
print(ans)

