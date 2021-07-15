def solution(n):
    # 1
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    # 2
    for i in range(n):
        for j in range(i, n):
            # 3
            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 4
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer