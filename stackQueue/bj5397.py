#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    tmp = input().rstrip()
    pwd,right=[],[]
    for i in tmp:
        if i=='<':
            if pwd:
                right.append(pwd.pop())
        elif i=='>':
            if right:
                pwd.append(right.pop())
        elif i=='-':
            if pwd:
                pwd.pop()
        else:
            pwd.append(i)

    print("".join(pwd)+"".join(reversed(right)))
