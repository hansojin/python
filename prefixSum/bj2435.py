#!/usr/bin/env python

n,k=map(int,input().split())
li=list(map(int,input().split()))
total=[]

for i in range(n-k+1):
    tot=0
    for j in range(i,i+k):
        tot+=li[j]
    total.append(tot)
print(max(total))
