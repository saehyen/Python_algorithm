n = int(input())
k = []
while n :
    a = int(input())
    k.append(a)
    n -= 1

k.sort(reverse=(True))

num = 0
result = 0
max = 0
for i in k :
    num += 1
    result = num * i

    if result > max :
        max = result

print(max)