#!/usr/bin/env python

mod=1000000007
p=15*pow(10,5)
def fibo(n):
    fib=[0,1]
    for i in range(2,p):
        fib.append(fib[i-2]+fib[i-1])
        fib[i]%=mod
    return fib[n%p]

n=int(input())
print(fibo(n))
