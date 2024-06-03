def solution(babbling):
    cnt=0
    for i in babbling:
        i=i.replace('aya','*')
        i=i.replace("ye",'*')
        i=i.replace('woo','*')
        i=i.replace("ma",'*')
        if i.count("*")==len(i):
            cnt+=1
    return cnt
