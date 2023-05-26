#!/usr/bin/env python

n=str(input())
cnt=0

while True:
    if len(n)==1:
        break
    else:
        cnt+=1
        summ=0
        for i in n:
            summ+=int(i)
        n=str(summ)
print(cnt)
if n=='3' or n=='6' or n=='9':
    print('YES')
else:
    print('NO')
