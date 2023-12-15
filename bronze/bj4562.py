#!usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    x,y=map(int,input().split())
    if y>x:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
