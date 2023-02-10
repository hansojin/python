#!/usr/bin/env python


import sys
input = sys.stdin.readline
from math import gcd

n=int(input())

nums=list(map(int,input().split()))
for i in range(1,n):
    print('{}/{}'.format(int(nums[0]/gcd(nums[i],num[0])),int(nums[i]/gcd(nums[i],nums[0]))

