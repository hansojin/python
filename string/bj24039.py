#!/usr/bin/env python

n=int(input())

li = [2,3]

def isPrime(n):
    while True:
        n+=1
        for i in range(2,n):
            if(n%i==0):
                break
        i+=1
        if i==n:
            return n

idx =2
while True:
    prev = li[idx-1]*li[idx-2]
    if(prev<=n):
        li.append(isPrime(li[-1]))
        idx+=1
    else:
        print(prev)
        break

