#!/usr/bin/env python

import sys
input= sys.stdin.readline

def check(n):
    strn = str(n)[::-1]
    tmp = str(int(strn)+n)
    tlen = len(tmp)
    flag = True
    for i in range(tlen//2):
        if tmp[i]==tmp[tlen-i-1]:
            continue
        else:
            flag = False
            break
    
    if flag:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    n=int(input())
    print(check(n))
