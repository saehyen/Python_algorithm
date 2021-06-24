# n = 물이 새는 곳 개수, l= 테이프 길이
n,l = map(int,input().split())
result = n
array= list(map(int,input().split()))
array.sort()
start = array[0]

for i in array :
    if start + l >= i + 0.5:
        result -= 1

    else:
        start = i - 0.5

print(result+1)