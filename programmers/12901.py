def solution(a, b):
    d=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    day=b
    for i in range(a):
        day+=d[i]
    print(day)
    y=['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    return y[day%7]
