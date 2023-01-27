#!/usr/bin/env python

num = [i for i in range(1,31)]

for _ in range(28):
    data = int(input())
    num.remove(data)

print(min(num), max(num))
