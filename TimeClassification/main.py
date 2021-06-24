n = int(input())
result = 0

# 탐색기법.
# 0시~n시 = n+1
for i in range(n + 1):
    # 60분
    for j in range(60):
        # 60초
        for k in range(60):
            # 3이 있는지 검색
            if '3' in str(i) + str(j) + str(k) :
                result += 1


print(result)