#!/usr/bin/env python

p=str(input())
for i in p:
    print(ord(i)-64, end=' ')
    # itoa -> chr(65)
    # A 65 a 97 (alpha 26)
