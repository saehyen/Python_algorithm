# 단순무식구현(fail)
n = int(input())
ans = 0
cnt = 665
def check(num):
    num = str(num)
    for i in range(len(num)-2) :
        print(num)
        if (num[i] == num[i+1] == num[i+2] == '6') :
            return True
    else :
        return False
while n != ans :
    cnt += 1
    if check(cnt) :
        ans += 1
    if ans == n :
        print(cnt)
    
   
    