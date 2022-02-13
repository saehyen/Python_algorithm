def dfs(cnt, result, add, sub, mul, div):
    global max_v
    global min_v
    if cnt == n:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return
    # 사칙연산의 수가 남아있을 경우
    if add > 0:
        dfs(cnt + 1, result + num_list[cnt], add-1, sub, mul, div)
    if sub > 0:
        dfs(cnt + 1, result - num_list[cnt], add, sub-1, mul, div)
    if mul > 0:
        dfs(cnt + 1, result * num_list[cnt], add, sub, mul-1, div)
    if div > 0:
        dfs(cnt + 1, -((-result) // (num_list[cnt])) if result < 0 else result // num_list[cnt] , add, sub, mul, div-1)
 
n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_v = -1000000001
min_v = 1000000001
dfs(1, num_list[0], add, sub, mul, div)
print(max_v)
print(min_v)