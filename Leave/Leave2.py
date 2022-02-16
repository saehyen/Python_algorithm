# DP를 이용한 풀이
n = int(input())
time = []
money = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)
    dp.append(b)
dp.append(0)
# 뒤에서 앞으로가며 반복문
for i in range(n-1,-1,-1):
    # 시간조건을 만족한다면
    if time[i] + i > n:
        dp[i] = dp[i+1]
    else:
        # 만족하지 않는다면 최대값 변경
        dp[i] = max(dp[i+1], money[i] + dp[i+time[i]])
print(dp[0])