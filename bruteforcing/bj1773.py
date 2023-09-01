#!/usr/bin/env python


n,c= map(int,input().split())
s=[0]*(c+1)
for _ in range(n):
    m=int(input())
    if m==1:
        print(c)
        exit()

    for i in range(m,c+1,m):
        s[i]=1
print(sum(s))
