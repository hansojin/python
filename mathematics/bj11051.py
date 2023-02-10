#!/usr/bin/env python

res=1
a,b=map(int,input().split())
for i in range(a-b+1,a+1):
    res*=i
for j in range(1,b+1):
    res/=j
print(int(res%10007))
