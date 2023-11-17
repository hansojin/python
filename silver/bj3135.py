#!/usr/bin/env python

a,b=map(int,input().split())
likes=[]
n=int(input())
for _ in range(n):
    likes.append(int(input()))

minn=1e9
for i in likes:
    if abs(i-b)<abs(minn-b):
        minn=i

res=1
if minn>b:
    res+=minn-b
else:
    res+=b-minn

if abs(a-b)<res:
    print(abs(a-b))
else:
    print(res)
