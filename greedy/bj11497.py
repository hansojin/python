#!/usr/bin/env python

import sys
input= sys.stdin.readline

for i in range(int(input())):
    n=int(input())
    t=list(map(int,input().split()))
    t.sort()
    ans=0

    for j in range(2,n):
        ans=max(ans,abs(t[j]-t[j-2]))
    print(ans)
