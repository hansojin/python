#!/usr/bin/env python

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    a,b=map(str,input().split())
    a_li=list(map(str,str(a)))
    a_li.sort()
    b_li=list(map(str,str(b)))
    b_li.sort()
    ans=True
    if len(a_li)!=len(b_li):
        ans=False
    if ans:
        for i in range(min(len(a_li),len(b_li))):
            if a_li[i]==b_li[i]:
                continue
            else:
                ans=False
                break
    if ans==True:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')




