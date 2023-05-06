#!/usr/bin/env python

v=['a','e','i','o','u','A','E','I','O','U']
while True:
    cnt=0
    sen=input()
    if sen=='#':
        break
    else:

        for i in sen:
            if i in v:
                cnt+=1
    print(cnt)
