#!/usr/bin/env python

n=int(input())

ans=10000
a=n//5+1
b=n//3+1

for i in range(a):
    for j in range(b):
        if(5*i + 3*j==n):
            if ans>i+j:
                ans=i+j
                
if ans==10000: print(-1)
else: print(ans)
