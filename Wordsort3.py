import sys
n = int(sys.stdin.readline())
x = []
x2 = []
for i in range(n):
    word = sys.stdin.readline().strip()
    if word not in x2:
        x2.append(word)
        x.append([word, len(word)])

# 1차원 배열 : x = list(set(x))
# 알파벳 순서대로 정렬
x.sort(key=lambda x:(x[1],x[0]))

# 길이별로 정렬
for i in x:
    print(i[0])