#!usr/bin/env python

n=int(input())
res=0

for _ in range(n):
    a,b,=map(int,input().split())
    res+=a*b
print(res)
