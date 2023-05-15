n=int(input())

for i in range(1,n+1):
    dash=0
    j=str(i)
    if '3' in j or '6' in j or '9' in j:
        dash+=j.count('3')
        dash+=j.count('6')
        dash+=j.count('9')
        for _ in range(dash):
            print('-', end='')
        print(' ',end='')
    else:
        print(i, end=' ')
