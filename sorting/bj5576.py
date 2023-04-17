#!/usr/bin/env python

import sys
input = sys.stdin.readline

ans=[]
for _ in range(2):
    tmp=[]
    for _ in range(10):
        num=int(input())
        tmp.append(num)

    tmp.sort(reverse=True)
    ans.append(sum(tmp[0:3]))
print(*ans)
