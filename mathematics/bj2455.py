#!/usr/bin/env python

on = []
p = 0

for _ in range(4):
    a, b = map(int, input().split())
    p += b
    p -= a
    on.append(p)

print(max(on))
