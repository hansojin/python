#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    ans=0
    n=int(input())
    li=list(map(int,input().split()))
    li.sort(reverse=True)
    for i in range(n):
        ans+=li[i]*(i+1)
    print(ans)
