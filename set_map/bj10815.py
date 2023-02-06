#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
n_li=list(map(int,input().split()))


m=int(input())
m_li=list(map(int,input().split()))

ans=[]
for i in range(m):
    if m_li[i] in n_li:
        ans.append(1)
    else:
        ans.append(0)

print(ans)
