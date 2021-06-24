n = int(input())
time = sorted([tuple(map(int, input().split()))for _ in range(n)], key=lambda x:(x[1], x[0]))
ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
        print(ans)
