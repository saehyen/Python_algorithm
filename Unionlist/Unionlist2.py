import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)