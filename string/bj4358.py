#!/usr/bin/env python

import sys
input= sys.stdin.readline

li={}
cnt=0
while True:
    n=input().strip()
    #if n.strip()=='':
    if not n:
        break
    else:
        if n in li:
            li[n]+=1
        else:
            li[n]=1
        cnt+=1

sort=sorted(li.items())
for i in sort:
    print(f'{i[0]} {(i[1]/cnt)*100:.4f}')
    
    

