from sys import stdin


n, m = map(int, stdin.readline().split())

cards = []
cards += map(int, stdin.readline().split())

for _ in range(m):
    cards.sort()
    cards[0] = cards[1] = cards[0] + cards[1]

print(sum(cards))