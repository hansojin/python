#!/usr/bin/env python

score=[100,100,200,200,300,300,400,400,500]
li=list(map(int,input().split()))
flag=True
if sum(li)<100:
    print("none")
else:
    for i in range(9):
        if score[i]<li[i]:
            flag=False
            break
    if flag:
        print("draw")
    else:
        print("hacker")
