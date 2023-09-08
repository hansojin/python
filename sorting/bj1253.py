#!/usr/bin/env python

import sys
input= sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

ans = 0
for i in range(n):
    tmp = arr[:i] + arr[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == arr[i]:
            ans += 1
            break
        if t < arr[i]: left += 1 
        else: right -= 1 
print(ans)


