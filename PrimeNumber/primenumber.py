# 시간초과 답
def sosu(num) :
    for i in range(2,num-1):
        if num%i == 0 :
            return False
    else :
        return True
a,b = map(int,input().split())
for i in range(a,b+1):
    if sosu(i) == True :
        print(i)
