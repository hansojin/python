#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
ans=[]
for _ in range(n):
    line=input().split()
    ans.append(line)
    # ans.append(list(input().split()))

ans.sort(key=lambda x :int(x[0]))
for i in range(n):
    print(ans[i][0], ans[i][1])
    
