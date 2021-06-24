import sys
n,k = map(int,input().split())
a= []
b= []
i = 0
sum = 0
for i in range (n) :
    weight,price = map(int,sys.stdin.readline().split())
    a.append([price,weight])

a.sort(reverse=True)
a.append([0,0])
for i in range(k):
    bag_weight = int(sys.stdin.readline())
    b.append(bag_weight)
b.sort(reverse=True)
for j in b:
    for i in a :
        if i[1] <= j:
            sum += i[0]
            a.remove(i)
            a.append([0,0])
            break
print(sum)

