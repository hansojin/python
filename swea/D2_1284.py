#!/usr/bin/env python

cases=int(input())
for case in range(cases):
    p,q,r,s,w=map(int,input().split())
    a=p*w
    b=q
    if w>r:
        b=q+(w-r)*s
    print(f'#{case+1} {min(a,b)}')


