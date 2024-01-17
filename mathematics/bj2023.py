#!/usr/bin/env python

import sys
input = sys.stdin.readline

N = int(input())

def isPrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solve(num):
    if len(str(num)) == N:
        if isPrimeNumber(num) == True:
            print(num)
        return
    
    for i in range(10):
        k = num*10 + i
        if isPrimeNumber(k) == True:
            solve(k)

for i in [2, 3, 5, 7]:
    solve(i)
