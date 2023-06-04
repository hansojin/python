#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

while True:
    nums=list(map(int,input().split()))
    if nums[0]==0:
        break
    del nums[0]
    nCr=list(combinations(nums,6))
    for i in nCr:
        for j in i:
            print(j,end=' ')
        print()
    print()
