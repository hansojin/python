#!/usr/bin/env python

a,b,c=map(int,input().split())
year=1

while True:
    if (year-a)%15==0 and (year-b)%28==0 and (year-c)%19==0:
        break
    year+=1
print(year)
