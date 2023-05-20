#!/usr/bin/env python

cases=int(input())
for case in range(cases):
    date=str(input())
    year=date[0:4]
    flag=1
    month,day=0,0
    if 1<=int(date[4:6])<=12:
        month=date[4:6]
    else:
        flag=0
        

    one=['01','03','05','07','08','10','12']
    zero=['04','06','09','11']
    if month in one:
        if int(date[6:8])<=31:
            day=date[6:8]
        else:
            flag=0
    elif month in zero:
        if int(date[6:8])<=30:
            day=date[6:8]
        else:
            flag=0
    elif month=='02':
        if int(date[6:8])<=28:
            day=date[6:8]
        else:
            flag=0

        
    
    if flag==0:
        print(f'#{case+1} -1')
    else:
        print(f'#{case+1} {year}/{month}/{day}')


