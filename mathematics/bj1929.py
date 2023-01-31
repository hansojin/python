#!/usr/bin/env python

a,b=map(int,input().split())


def prime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):   #num의 제곱근까지만 계산. 그 이후는 하나마나라 그렇대
            if num%i==0:
                return False
            
        return True

for i in range (a,b+1):
    if prime(i):
        print(i)
