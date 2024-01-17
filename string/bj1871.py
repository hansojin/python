#!/usr/bin/env python

import sys
input= sys.stdin.readline

def abc(word):
    tmp=0
    for i in range(3):
        tmp+=(ord(word[i])-65)*(26**(2-i))
    return tmp
for _ in range(int(input())):
    a,n=input().split('-')
    a,n=abc(a),int(n)
    if abs(a-n) <=100:
        print("nice")
    else:
        print("not nice")
