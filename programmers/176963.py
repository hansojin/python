def solution(name, yearning, photo):
    answer = []
    dic=dict()
    for i in range(len(name)):
        dic[name[i]]=yearning[i]
    for ph in photo:
        tmp=0
        for x in ph:
            if x in dic:
                tmp+=dic[x]
        answer.append(tmp)
    return answer
