#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
num=list(set(list(map(int,input().split()))))

num.sort()
print(*num)

