#!/usr/bin/env python

x,y,w,h=map(int,input().split())

print(min(x,y,w-x,h-y))
