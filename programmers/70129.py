def solution(s):
    cnt,zeroCnt = 0,0  

    while True:
        if s == "1":
            break;
            
        zeroCnt += s.count("0")  
        s = s.replace("0",'')    
        s = bin(len(s))[2:]      
        cnt +=1

    return [cnt, zeroCnt]   
