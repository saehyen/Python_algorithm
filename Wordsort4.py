import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]
for i in sorted(set(words), key=lambda x: (len(x), x)):
    print(i)