#!/usr/bin/env python

import sys
input= sys.stdin.readline

dic=dict()
n,m,k=map(int,input().split())
for _ in range(n):
    a,b=input().split()
    dic[a]=int(b)
show=0
for _ in range(k):
    sub=input().rstrip()
    show+=int(dic[sub])
    del(dic[sub])

values = sorted(list(dic.values()))

more = m-k
if more==0:
    print(show,show)
else:
    print(show+sum(values[:more]),show+sum(values[-more:]))
