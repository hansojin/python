#!/usr/bin/env python

import sys
input= sys.stdin.readline

def isAlpha(n):
    n=ord(n)
    if 97<=n<=122:
        return True
    else:
        return False
li=[]
for _ in range(int(input())):
    tmp=""
    word=input().rstrip()+"a"
    for i in range(len(word)-1):
        if isAlpha(word[i]):
            if len(tmp)!=0:
                li.append(int(tmp))
                tmp=""
        else:
            tmp+=word[i]
    if len(tmp)!=0:
        li.append(int(tmp))
li.sort()
for i in li:
    print(i)
        
