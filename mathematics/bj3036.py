#!/usr/bin/env python

from fractions import Fraction as fr
import sys
input = sys.stdin.readline


n=int(input())

nums=list(map(int,input().split()))
for i in range(1,n):
    ans=fr(nums[0],1)/fr(nums[i],1)
    print(ans.numerator,'/',ans.denominator,sep='')

