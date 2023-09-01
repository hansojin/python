#!/usr/bin/env python

while True:
    word=input()
    if word=='#':
        break
    cnt=0
    value=word[0]
    data =word[2::]
    
    print(value,data.count(value)+data.count(value.upper()))
