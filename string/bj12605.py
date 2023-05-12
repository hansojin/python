#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())

for i in range(1,n+1):
    tmp=list(map(str,input().rstrip().split()))
    print(f'Case #{i}: ',end='')
    for i in tmp[::-1]:
        print(i,end=' ')
    print()
    
