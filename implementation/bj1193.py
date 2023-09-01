#!/usr/bin/env python

n=int(input())

l,e=0,0
while n>e:
    l+=1
    e+=l
diff = e-n
if l%2==0:
    top=l-diff
    bot=diff+1
else:
    top=diff+1
    bot=l-diff
print("%d/%d"%(top,bot))
