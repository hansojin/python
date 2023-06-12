#!/usr/bin/env python

n=int(input())
tmp=list(map(int,input().split()))
srt=sorted(tmp)
li=[]
for i in range(n):
    idx=srt.index(tmp[i])
    li.append(idx)
    srt[idx]=-1
print(*li)



