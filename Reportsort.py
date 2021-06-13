import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(sys.stdin.readline().split())
array.sort(key=lambda array:(-int(array[1]),int(array[2]),-int(array[3]),array[0]))

for i in array:
    print(i[0])