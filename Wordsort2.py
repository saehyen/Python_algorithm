import sys
n = int(sys.stdin.readline())
x = []
for i in range(n):
    x.append(sys.stdin.readline().strip())
# 중복된 값을 제거하기위해 set 자료형으로 바꿨다가 다시 list 형태로 바꿈
x = list(set(x))
# 알파벳 순서대로 정렬
x.sort()
# 길이별로 정렬
for i in x:
    for j in range(len(x)-1):
        if len(x[j]) > len(x[j+1]):
            x[j], x[j+1] = x[j+1], x[j]

for i in x:
    print(i)