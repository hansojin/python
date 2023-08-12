#!/usr/bin/env python

import sys
input= sys.stdin.readline

def dayy(y,m,d):
    return int(y),int(m),int(d)

y,m,d=map(str,input().split('-'))
y,m,d= dayy(y,m,d)

cnt=0
for _ in range(int(input())):
    year, month, day = map(str,input().split('-'))
    year,month,day=dayy(year,month,day)

    if y<year:
            cnt+=1
    elif y==year:
        if m<month:
            cnt+=1
        elif m==month:
            if d<=day:
                cnt+=1
            

print(cnt)
    
