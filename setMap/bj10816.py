#!/usr/bin/env python


import sys
from collections import Counter
input=sys.stdin.readline

n = int(input())
n_li = list(map(int,input().split()))

m = int(input())
m_li = list(map(int,input().split()))

c=Counter(n_li)

for i in m_li:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')
