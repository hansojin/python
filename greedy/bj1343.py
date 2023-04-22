#!/usr/bin/env python

li=input()
li=li.replace('XXXX','AAAA')
li=li.replace('XX','BB')

if 'X' in li:
    print(-1)
else:
    print(li)
