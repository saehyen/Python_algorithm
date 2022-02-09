n = int(input())
# 시작점 구하기
start_5 = n//5
start_3 = 0
answer = -1

# 만약 5로 나눴을때 
while(n!=0 and (start_5 != -1)):
    res_n = n - (start_5 * 5)
    if res_n % 3 == 0 :
        answer =  res_n/3 + start_5
        break
    else :
        #print("남은숫자 :" + str(res_n) + "& 5봉지 : " + str(start_5))
        start_5 -= 1

print(int(answer))
