
def deSum(n) :
    numstr = str(n)
    s = n
    for i in range(len(numstr)) :
        s += int(numstr[i])
    return s

def findCon(m) :
    for i in range(m) :
        if m == deSum(i) :
            return i
    return 0

n = int(input())
print(findCon(n))

