n, m = map(int,input().split())
A,B = [], []

for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
A = set(A)
B = set(B)
C = A & B
print(len(C))
for i in sorted(C):
    print(i)