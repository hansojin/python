#!/usr/bin/env python

import sys
input= sys.stdin.readline

for i in range(int(input())):
    a,b=map(int,input().split())
    print(f'You get {a//b} piece(s) and your dad gets {a%b} piece(s).')
