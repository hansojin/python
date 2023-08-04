#!/usr/bin/env python

import sys
input= sys.stdin.readline
mod = 1000000007
n=int(input())
li=sorted(list(map(int,input().split())))

ans=0

def pow(a,b):
    if b==0:
        return 1
    if b==1:
        return a

    hf = pow(a,b//2)
    return hf*hf%mod if b%2==0 else hf*hf*a%mod

for i in range(n):
    ans+= li[i]*(pow(2,i) - pow(2,n-i-1))
print(ans%mod)
