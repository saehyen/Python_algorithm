import sys
N = int(input())
arr = []
for i in range(N):
        age, name = map(str, sys.stdin.readline().split())
        age = int(age)
        arr.append((age, name))
# 그냥 이름순으로 정렬해도 들어온 순서대로 정렬됨.
arr.sort(key=lambda key_value : key_value[0])
for i in arr:
        print(i[0], i[1])