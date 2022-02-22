n = int(input())
sentences = []
for i in range(n):
    string = list(input().split())
    for j in string:
        print(j[::-1],end=' ')
    