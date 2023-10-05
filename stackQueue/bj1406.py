#!/usr/bin/env python

import sys 
input= sys.stdin.readline

ls=list(input().rstrip())
rs=[]
for _ in range(int(input())):
    order = input()
    if order[0]=='L':
        if ls!=[]:
            rs.append(ls.pop())
    elif order[0]=='D':
        if rs!=[]:
            ls.append(rs.pop())
    elif order[0]== 'B':
        if ls:
            ls.pop()
    elif order[0]=='P':  
        ls.append(order[2])
print(''.join(ls),end='')
print(''.join(list(reversed(rs))),end='')

                        
# del, insert 는 시간초과
# left stack, right stack 을 사용해서, 
# 커서를 왼쪽으로 옮기면, left stack top을 right stack으로 (vice versa)
# 문자를 지운다면 left stack의 top을 지우는, 추가한다면 left top 에 추가
