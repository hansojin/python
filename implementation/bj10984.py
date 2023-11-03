#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    cnt,sum=0,0
    for _ in range(int(input())):
        a,b=input().split()
        cnt+=int(a)
        sum+=float(b)*int(a)
    print(cnt, round(sum/cnt,1))
