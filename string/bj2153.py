#!/usr/bin/env python

import sys
input= sys.stdin.readline

word=input().rstrip()

def isPrime(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
ans=0
for i in word:
    if 'a'<=i<='z':
        ans+=(ord(i)-96)
    else:
        ans+=(ord(i)-38)

if isPrime(ans):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
