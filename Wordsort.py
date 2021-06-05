import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
    word = sys.stdin.readline().strip()
    if word not in x:
        x.append(word)

x.sort()
for i in x:
    for j in range(len(x)-1):
        if len(x[j]) > len(x[j+1]):
            x[j], x[j+1] = x[j+1], x[j]

for i in x:
    print(i)