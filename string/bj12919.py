#!/usr/bin/env python

import sys
input= sys.stdin.readline

s = input()
t = input()

ans = 0
def sub(str1, trgt):
    global ans
    if len(str1) == len(trgt):
        if trgt == str1:
            ans = 1
        return
    if trgt[-1] == 'A':
        sub(str1, trgt[:-1])
    if trgt[0] == 'B':
        sub(str1, trgt[:0:-1])

sub(s, t)
print(ans)
