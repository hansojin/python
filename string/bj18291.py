#!/usr/bin/env python

for _ in range(int(input())):
    n=int(input())
    x,ans=2,1
    n-=2
    mod = 10**9+7

    if n<0:
        print(1)
    else:
        while n:
            if n&1:
                ans*=x
                ans%=mod
            n//=2
            x*=x
            x%=mod
        print(ans)
