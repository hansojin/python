#!/usr/bin/env python

import sys
for _ in range(int(input())):
    even=0
    minn=sys.maxsize
    li=list(map(int,input().split()))
    for i in li:
        if i%2==0:
            even+=i
            if minn>i:
                minn=i
    print(even, minn)
