#!/usr/bin/env python

x, y, c = map(float, input().split())
s, e = 0, min(x, y)
while e-s > 0.000001:
    m = (s+e)/2
    h1 = (x**2-m**2)**0.5
    h2 = (y**2-m**2)**0.5    
    h = h1*h2 / (h1+h2)
    if h >= c:
        res = m
        s = m
    else:
        e = m
print(res)
