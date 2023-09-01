#!/usr/bin/env python

import sys
input= sys.stdin.readline
n = int(input().rstrip())
li = list(map(int,input().split()))

ans = 0
for i in range(len(li)) :
    tmp = 0
    for j in range(i,len(li)) :
        tmp += abs(li[i] - li[j])
    ans += tmp*2

print(ans)
