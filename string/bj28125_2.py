#!/usr/bin/env python

import sys
input = sys.stdin.readline

d = {'@':'a', '[':'c', '!':'i', ';':'j', '^':'n', \
     '0':'o', '7':'t', "\\\\'": 'w', "\\'":'v'}

n = int(input())
for _ in range(n):
    s = input().rstrip()
    cnt = 0
    for ss in s:
        if not ss.isalpha() and ss != "\\":
            cnt += 1

    for key in d:
        s = s.replace(key, d[key])
    if cnt >= (len(s) + 1) // 2: 
        print("I don't understand")
    else: 
        print(s)
