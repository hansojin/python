#!/usr/bin/env python

coin=[25,10,5,1]
for _ in range(int(input())):
    li=[]
    num=int(input())
    for coins in coin:
        li.append(num//coins)
        num=num%coins
    print(*li)
