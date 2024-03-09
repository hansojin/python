#!/usr/bin/env python

import sys
input= sys.stdin.readline

def histogram(n,read):
    stack=[]
    s=0
    read.append(0)

    for i in range(n+1):
        val=read[i]
        start=i
        while stack and stack[-1][1]>=val:
            start,pre=stack.pop()
            s=max(s,(i-start)*pre)
        stack.append([start,val])
    print(s)

while True:
    read=list(map(int,input().split()))
    n=read[0]
    if n==0:
        break
    histogram(n,read[1:])
