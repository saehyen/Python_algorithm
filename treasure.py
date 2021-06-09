n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A정렬, B정렬 후 sum에 더해주는 식
A.sort()
B.sort(reverse=True)
sum = 0
for i in range(n):
    sum += A[i]*B[i]
print(sum)