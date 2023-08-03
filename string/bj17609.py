#!/usr/bin/env python

import sys
input= sys.stdin.readline

def check(s,e):
    while s<e:
        if word[s]==word[e]:
            s+=1
            e-=1
        else:
            return False
    return True

def twoPtr(s,e):
    while s<e:
        if word[s]==word[e]:
            s+=1
            e-=1
        else:
            if check(s+1,e) or check(s,e-1):
                return 1
            return 2
    return 0



for _ in range(int(input())):
    word=input()
    print(twoPtr(0,len(word.rstrip())-1))
