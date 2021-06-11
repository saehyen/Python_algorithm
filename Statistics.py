from collections import Counter
import sys


def modefinder(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

n = int(sys.stdin.readline())
array = []
sum = 0
for i in range(n):
    x = int(sys.stdin.readline())
    array.append(x)
    sum += x
array.sort()

# 산술평균
avg = sum // n
print(round(avg))

# 중앙값 산출
mid = len(array)//2
print(array[mid])

# 최빈값
cnt = modefinder(array)
print(cnt)

# 범위
range = max(array) - min(array)
print(range)


