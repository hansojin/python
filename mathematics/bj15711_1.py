#!/usr/bin/env python

import sys
input = sys.stdin.readline

def power(base, exp, r):
    if exp==1: 
        return base%r
    elif exp%2 ==0:
        temp = power(base, exp//2, r)
        return (temp*temp) % r
    else:
        return (power(base,exp-1,r)*base)%r

def is_prime(num):
    if num == 1: 
        return False
    elif num < 1000000: 
        upper = int(num**0.5)+1
        for j in range(2, upper):
            if num%j == 0: 
                return False
        return True
    else : 
        for p in [2, 3, 5, 7, 11]:
            passed = False
            d = (num - 1)//2
            while d % 2 == 0:
                if power(p, d, num) == num-1: 
                    passed = True
                d //= 2
            last = power(p, d, num)
            if last == 1 or last == num-1: 
                passed = True
            if not passed: 
                return False
        return True

for _ in range(int(input())):
    a, b=map(int, input().split())
    if a+b==2: 
        print('NO')
    elif (a+b)%2==0: 
        print('YES')
    else :
        if is_prime(a+b-2): 
            print('YES')
        else: 
            print('NO')
