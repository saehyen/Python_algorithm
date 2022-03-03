from itertools import combinations
while True :
    tmp = list(map(int,input().split()))
    if tmp[0] == 0 :
        break
    numbers = tmp[1:]
    answers = list(combinations(numbers, 6))
    
    for i in answers:
        for j in i:
            print(j, end=' ')
        print()
    print()

