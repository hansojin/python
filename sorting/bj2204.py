#!/usr/bin/env python

while True:
    n=int(input())
    if n==0:
        break
    else:
        li=[]
        for _ in range(n):
            tmp=input()
            li.append((tmp,tmp.lower()))
            li= sorted(li,key=lambda x : x[1])
            
        print(li[0][0]) 
