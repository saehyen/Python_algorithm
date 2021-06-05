import sys

n = int(sys.stdin.readline())
x = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    x.append([age, name, i])

x.sort(key=lambda x: (x[0], x[2]))
for i in x:
    print(i[0], i[1])