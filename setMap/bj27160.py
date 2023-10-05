#!/usr/bin/env python

dict={'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}

for i in range(int(input())):
    a,b=input().split()
    dict[a]+=int(b)
flag= False

for i in dict.values():
    if i==5:
        flag=True
if flag:
    print("YES")
else:
    print("NO")
