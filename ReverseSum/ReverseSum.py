a,b = map(int,input().split())
A = str(a)[::-1]
B = str(b)[::-1]
answer = str(int(A) + int(B))[::-1]
print(int(answer))