def solution(s):
    tmp=[]
    for i in s:
        if i =='(':
            tmp.append(i)
        else:
            if tmp:
                tmp.pop()
            else:
                return False
    if tmp:
        return False
    return True
