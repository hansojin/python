#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,k=map(int,input().split())
p = 1000000007

def fac(num, mod):
    result = 1
    for i in range(2, num+1):
        result = result * i % p
    return result

def power(num, p, mod):
    if p == 1:
        return num % mod
    
    if p % 2:
        return ((power(num,p//2,mod) ** 2) * num) % mod
    else:
        return (power(num,p//2,mod) ** 2) % mod
    
print(fac(n, p) * power((fac(k, p) * fac(n-k, p)), p-2, p) % p)


