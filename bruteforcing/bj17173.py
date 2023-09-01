#!/usr/bin/env python

n,m=map(int,input().split())
tmp = list(map(int,input().split()))

li=[0 for _ in range(n+1)]
ans=0
for i in tmp:
    for j in range(i,n+1,i):
        if li[j]!=1:
            ans+=j
            li[j]=1
print(ans)
