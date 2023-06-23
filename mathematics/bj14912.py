#!/usr/bin/env python

n,m=map(int,input().split())
cnt=0
for i in range(1,n+1):
    i=str(i)
    for j in range(len(i)):
        if i[j]==str(m):
            cnt+=1
print(cnt)
