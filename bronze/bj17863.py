#!/usr/bin/env python

n=input()
if len(n)==7:
    if n[:3]=='555':
        print("YES")
    else:
        print("NO")
else:
    print("NO")
