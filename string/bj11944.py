#!/usr/bin/env python

n,m=map(int,input().split())
tmp = len(str(n))
if tmp*n>=m:
    cnt=m//tmp
    mod=m%tmp
    for _ in range(cnt):
        print(n,end='')
    if mod!=0:
        strn=str(n)
        print(strn[:mod])
else:
    for _ in range(n):
        print(n,end='')

