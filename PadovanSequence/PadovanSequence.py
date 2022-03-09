# DP
DP = [0 for i in range(101)]
DP[1] = 1
DP[2] = 1
DP[3] = 1
for i in range(0, 98):
    DP[i + 3] = DP[i] + DP[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(DP[n])