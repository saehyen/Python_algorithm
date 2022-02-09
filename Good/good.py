# 타임오바 답
n = int(input())
num = list(map(int,input().split()))
answer = []
sumnum = 0
num.sort()
for i in range(n):
    for j in range(i+1,n-1):
        sumnum = num[i] + num[j]
        # 중간
        if sumnum in num[i:j-1] or sumnum in num[j+1:]:
            answer.append(num[i] + num[j])
        
print(len(list(set(answer))))