def issosu(num):
    if num == 1 :
        return False
    for i in range(2,num):
        if num%i == 0 :
            return False
    else:
        return True
input()
numlist = list(map(int,input().split()))
answer = 0
for num in numlist :
    if issosu(num) == True :
        answer += 1
    else :
        continue
print(answer)