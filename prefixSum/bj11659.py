#!/usr/bin/env python

import sys
input = sys.stdin.readline


a,b=map(int,input().split())
li=list(map(int,input().split()))
def ran(m,n):
    ans=0
    for i in range(m-1,n):
        ans+=li[i]
    return ans

for i in range(b):
    m,n=map(int,input().split())
    print(ran(m,n))

