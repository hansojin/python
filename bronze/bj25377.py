#!/usr/bin/env python

import sys
input= sys.stdin.readline

minn=1001
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<=b:
        minn=min(b,minn)
if minn==1001:
    print(-1)
else:
    print(minn)
