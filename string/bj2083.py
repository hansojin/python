#!/usr/bin/env python

import sys
input= sys.stdin.readline

while True:
    name,age,w = input().split()
    if name=='#':
        break
    if int(age)>17 or int(w)>=80:
        print(name,"Senoir")
    else:
        print(name,"Junior")
