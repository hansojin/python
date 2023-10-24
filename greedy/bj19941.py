#!/usr/bin/env python

n,k=map(int,input().split())
li=list(input())
cnt=0
for i in range(n):
    if li[i]=='P':
        s,e=i-k,i+k
        if s<0:
            s=0
        if e>=n:
            e=n-1
        for j in range(s,e+1):
            if li[j]=='H':
                li[j]='x'
                cnt+=1
                break
print(cnt)
