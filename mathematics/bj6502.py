#!/usr/bin/env python

import sys
input = sys.stdin.readline

cnt=1
while True:    
    num=list(map(int,input().split()))
    if num[0]==0:
        break
    if (num[0]*2)**2 >= num[1]**2+num[2]**2:
        print("Pizza " + str(cnt) + " fits on the table.")
        cnt+=1
    else:
        print("Pizza " + str(cnt) + " does not fit on the table.")
        cnt+=1
