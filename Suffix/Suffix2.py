S = str(input())
S_list = []

for _ in S:
    S_list.append(S)
    S = S[1:]

for i in sorted(S_list):
    print(i)