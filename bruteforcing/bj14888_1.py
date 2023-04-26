from itertools import product

n=int(input())
nums=list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

def operate(perm):
  result=nums[0]
  for i in range(1,len(nums)):
    if(perm[i-1]=="+"):
        result+=nums[i]
    elif(perm[i-1]=="-"):
        result-=nums[i]
    elif(perm[i-1]=="*"):
        result*=nums[i]
    elif(perm[i-1]=="/"):
        if(result<0):
            result=-1*((-1*result)//nums[i])
        else:
            result//=nums[i]
  return result

minimum=1e9
maximum=-1e9
    
for perm in list(product(['+','-','*','/'], repeat=(n - 1))):
    if(list(perm).count('+')>add):
        continue
    if(list(perm).count('-')>sub):
        continue
    if(list(perm).count('/')>div):
        continue
    if(list(perm).count('*')>mul):
        continue
     
    minimum=min(minimum,operate(list(perm)))
    maximum=max(maximum,operate(list(perm)))

print(maximum)
print(minimum)
