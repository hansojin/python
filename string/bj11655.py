#!/usr/bin/env python

word=input()

for i in word:
    if 65<=ord(i)<=90:
        tmp=ord(i)
        if ord(i)<78:
            print(chr(tmp+13),end='')
        else:
            print(chr(tmp-13),end='')
    elif 97<=ord(i)<=122:
        tmp=ord(i)
        if ord(i)<110:
            print(chr(tmp+13),end='')
        else:
            print(chr(tmp-13),end='')
    else:
        print(i,end='')
