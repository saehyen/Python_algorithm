n,k = map(int, input().split())
count = 0
coinlist = []
for i in range (0,n) :
    coin = int(input())
    coinlist.append(coin)

coinlist.sort(reverse=True)

for i in coinlist :
    while k >= i :
            k = k - i
            count += 1
            if n == 0:
                break

print(count)
