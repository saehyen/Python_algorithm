n = int(input())

for i in range(n) :
    brackets = list(input())
    check = 0
    for bracket in brackets :
        if bracket == '(' :
            check += 1
        elif bracket == ')' :
            check -= 1
        if check < 0:
            print('NO')
            break
    if check > 0 :
        print('NO')
    elif check == 0 :
        print("YES")