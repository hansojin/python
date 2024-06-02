def solution(lottos, win_nums):
    zeros = lottos.count(0)               
    win = 0                              
    scores = {0: 6, 1: 6, 2: 5, 3: 4,4: 3, 5: 2, 6: 1}                  
    for l in lottos:                    
        if l in win_nums:
            win += 1
    most = win + zeros
    least = win         
    return [scores[most], scores[least]]

