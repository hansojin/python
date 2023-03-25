#!/usr/bin/env python

import math

d,h,w=map(int,input().split())
x=math.sqrt((d*d)/(h*h+w*w))
print(math.floor(x*h),math.floor(x*w))
