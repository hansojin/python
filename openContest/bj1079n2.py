#!/usr/bin/env python

import sys
input= sys.stdin.readline

s=set()
s.add(' ')
n=int(input())
nl = input().split()
for i in range(len(nl)):
    s.add(nl[i])
m=int(input())
ml = input().split()
for i in range(len(ml)):
    s.add(str(ml[i]))
k=int(input())

kl = input()
for i in range(len(kl)):
    s.discard(kl[i])
ss=int(input())
word= input()
tmp=""
for i in range(ss):
    if word[i] in s:
        if len(tmp)>0:
            print(tmp)
        tmp=""
    else:
        tmp+=word[i]
        if i==ss-1:
            print(tmp)
