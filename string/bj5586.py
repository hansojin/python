#!/usr/bin/env python

import sys
input= sys.stdin.readline

word=input()
joi="JOI"
ioi="IOI"
jcnt,icnt=0,0
for i in range(len(word)-2):
    if word[i]=="J" and word[i+1]=="O" and word[i+2]=="I":
        jcnt+=1
    if word[i]=="I" and word[i+1]=="O" and word[i+2]=="I":
        icnt+=1
print(jcnt)
print(icnt)

