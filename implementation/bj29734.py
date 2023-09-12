#!/usr/bin/env python

a,b= map(int,input().split())
t,s= map(int,input().split())

jip, dok =a,b
atmp = a//8
if a%8==0:
    jip+=s*(atmp-1)
else:
    jip+=s*atmp

btmp = b//8
if b%8==0:
    dok+=t*(2*(btmp-1)+1)
    dok+=s*(btmp-1)
else:
    dok+=t*(2*btmp+1)
    dok+=s*btmp

if jip<dok:
    print('Zip')
    print(jip)
else:
    print("Dok")
    print(dok)

