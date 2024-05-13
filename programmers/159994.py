def solution(cards1, cards2, goal):
    flag=True
    a,b=0,0
    for g in goal:
        if g==cards1[a]:
            if a<len(cards1)-1:
                a+=1
        elif g==cards2[b]:
            if b<len(cards2)-1:
                b+=1
        else:
            flag=False
            break
    if flag:
        return "Yes"
    else:
        return "No"
