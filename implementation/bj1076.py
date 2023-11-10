#!/usr/bin/env python

color=['black','brown','red','orange','yellow','green','blue','violet','grey','white']

ans=0
f=input()
ans+=color.index(f)*10
s=input()
ans+=color.index(s)
l=input()
ans*=pow(10,color.index(l))
print(ans)

