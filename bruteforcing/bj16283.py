#!/usr/bin/env python

a,b,n,w=map(int,input().split())

li=[]
for i in range(1,n):
    x,y=i,n-i
    if a*x+b*y==w:
        li.append([x,y])
if len(li)==1:
    print(li[0][0],li[0][1])
else:
    print(-1)
