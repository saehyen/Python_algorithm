def check(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return 0
    return 1
N = int(input())
for i in range(N):
    N = int(input())
    for n in range(N, 0, -1):
        if check(str(n)):
            print(f"Case #{i+1}: {n}")
            break