#!/usr/bin/env python


y,m,d = input().split('-')
y,m,d=int(y),int(m),int(d)
n=int(input())
day=d+(n%30)
month=m+(n//30)
if day>30:
    day-=30
    month+=1
while month>12:
    month-=12
    y+=1

print(f"{y:04d}-{month:02d}-{day:02d}")


