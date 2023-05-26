#!/usr/bin/env python

n=int(input())
seat=str(input())
seat=seat.replace("LL","L")
holder=len(seat)+1
print(min(n,holder))
