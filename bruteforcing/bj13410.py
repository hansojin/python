#!/usr/bin/env python

n,m=map(int,input().split())
tmp=[]
for i in range(1,m+1):
    tmp.append(n*i)
li=[]
for i in tmp:
    i=str(i)
    li.append(int(i[::-1]))
print(max(li))
