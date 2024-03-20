#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    n=list(input().strip().replace(" ",""))
    if n[0]=='*':
        break
    n=list(set(n))
    n.sort()
    if 'abcdefghijklmnopqrstuvwxyz' == ''.join(n):
        print('Y')
    else:
        print("N")
