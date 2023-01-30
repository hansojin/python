alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word=input()

time=0
for chunk in alpha:
    for i in chunk: #청크에서 알바펫 하나씩 분리
        for x in word:  #입력 받은 단어에서 하나씩 분리
            if i==x:
                time+=alpha.index(chunk)+3
print(time)
