#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
edge=list(map(int,input().split()))
node = list(map(int,input().split()))

ans=0
m=node[0]
for i in range(n-1):
    if node[i]<m:
        m=node[i]
    ans+=m*edge[i]
print(ans)

