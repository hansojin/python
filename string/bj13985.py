#!/usr/bin/env python

fx=input().split('=')
if eval(fx[0])==int(fx[1]):
    print('YES')
else:
    print('NO')
