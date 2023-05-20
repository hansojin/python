#!/usr/bin/env python 

n=str(input())
al=list(map(str,str(n)))
for i in al:
    if i.isupper():
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
