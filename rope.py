n = int(input())
k = []
while n :
    a = int(input())
    k.append(a)
    n -= 1

k.sort(reverse=(True))
sum = 0
num = 0
result = 0
max = 0
for i in k :
    num += 1
    sum += i
    result = num * i
    if result > max :
        max = result

print(result)
print(r)