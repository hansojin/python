#!/usr/bin/env python

import sys
input= sys.stdin.readline

s=[]
b=[]
for _ in range(int(input())):
    std = input().rstrip()
    if std[:7]=='boj.kr/':
        b.append(int(std[7:]))
    else:
        s.append(std)
s.sort()
ss = sorted(s,key=len)
for i in ss:
    print(i)
b.sort()
for i in b:
    print(f'boj.kr/{i}')

