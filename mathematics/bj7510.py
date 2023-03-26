#!/usr/bin/env python

import sys
input = sys.stdin.readline
import math

for i in range(int(input())):
    a,b,c=map(int,input().split())
    
    print(f'Scenario #{i+1}:')
    if 2*math.pow(max(a,b,c),2)==math.pow(a,2)+math.pow(b,2)+math.pow(c,2):
        print('yes')
    else:
        print('no')
    print()

    
