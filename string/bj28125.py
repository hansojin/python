#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
#ch=['@','[','!',';','^','0','7',"\\'","\\\\'"]

for i in range(n):
    word=input()
    cnt=0
    for j in word:
        if j.islower():
            cnt+=1
    
    wrd=word.replace('@','a').replace('[','c').replace('!','i').replace(';','j').replace('^','n').replace('0','o').replace('7','t').replace("\\\\'",'w').replace("\\'",'v')
    
    if len(wrd)//2<len(wrd)-cnt:
        print("I don't understand",end='')
    else:
        print(wrd,end='')
