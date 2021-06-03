import sys
n,k = map(int,input().split())
a= []
b= []
i = 0
sum = 0
for i in range (n) :
    weight,price = map(int,sys.stdin.readline().split())
    a.append([price,weight])

a.sort(key = lambda x : (-x[0], -x[1]))
for i in range(k):
    bag_weight = int(sys.stdin.readline())
    b.append(bag_weight)
b.sort(reverse=True)


for j in b:
    for i in a:
        if j >= i[1]:
            sum += i[0]
            aindex= a.index(i)
            del a[:aindex]

    break

print(sum)