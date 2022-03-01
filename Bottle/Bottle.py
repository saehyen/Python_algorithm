N,K = map(int,input().split())
water = 0
while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    water += plus
    N += plus
print(water)