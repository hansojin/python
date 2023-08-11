#!/usr/bin/env python

n,l=input().split()
n=int(n)
cnt,N=0,0
while cnt!=n:
    N+=1
    if l in str(N):
        continue
    cnt+=1
print(N)
