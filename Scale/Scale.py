N = int(input())
result = []
sum = 1

chu = list(map(int,input().split( )))
chu.sort()
# 이전까지 더한 값보다 다음 값이 더 크면 break
for i in range(N) :
    if sum < chu[i] :
        break
    sum += chu[i]

print(sum)