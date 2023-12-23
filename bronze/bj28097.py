#!/usr/bin/env python

N = int(input())
s = list(map(int, input().split()))
t = sum(s) + (8 * (N-1))

d, t =  t// 24, t % 24

print(d, t)

