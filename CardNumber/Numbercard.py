# 상근이가 가진 카드 수
n = int(input())
# 상근이가 가진 카드
A = list(map(int, input().split()))
# 판별해야 될 카드 수
m = int(input())
# 판별해야 될 카드
B = list(map(int, input().split()))

C = [0] * m
for i in range(len(B)-1) :
    if B[i] in A:
        C[i] = 1
for i in C:
    print(i,end=' ')
