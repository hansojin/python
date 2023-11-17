#!/usr/bin/env python

li=[0]*101

n=input()
guest = list(map(int,input().split()))
cnt=0
for i in guest:
    if li[i]==1:
        cnt+=1
    else:
        li[i]=1
print(cnt)
