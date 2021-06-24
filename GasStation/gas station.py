N = int(input())

distance = list(map(int,input().split()))
station = list(map(int,input().split()))
num = 0
minstation = station[0]

result = 0
for i in station :
    if minstation < i :
        result += distance[num] * minstation
    else :
        minstation = i
        result += distance[num] * minstation
    num += 1
    if num == N - 1:
        break
print(result)