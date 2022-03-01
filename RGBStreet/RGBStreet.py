n = int(input())
prices = []

for i in range(n):
    prices.append(list(map(int,input().split())))

for i in range(1,len(prices)):
    # 첫집을 를 빨간색으로 칠했을 때
    prices[i][0] = min(prices[i-1][1],prices[i-1][2])+prices[i][0]
    # 첫집을 초록으로 칠했을 때
    prices[i][1] = min(prices[i-1][0],prices[i-1][2])+prices[i][1]
    # 첫집을 파랑으로 칠했을 때
    prices[i][2] = min(prices[i-1][0],prices[i-1][1])+prices[i][2]
print(min(prices[n-1][0],prices[n-1][1],prices[n-1][2]))
