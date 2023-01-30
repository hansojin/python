#!/usr/bin/env python

n=int(input())
nums=map(int,input().split())

ans=0
for i in nums:
    
    cnt=0
    for a in range(1,i+1):
        if i%a==0:
            cnt+=1
    if cnt==2:
        ans+=1
print(ans)
