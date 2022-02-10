# 배열 사용안하고 풀려고 한 방법
N = int(input())
answer = 0
min = int(input())
for i in range(N-1) :
    a = int(input())
    if min >= a :
        b = min-a
        a = a+b+1
        min = a
        answer += b+1
    else:
        min = a
print(answer)