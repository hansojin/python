def solution(n):
    li=[0,1]
    if n<2:
        return li[n]
    else:
        for i in range(n-1):
            li.append(li[-1]+li[-2])
        return li[-1]%1234567
            
