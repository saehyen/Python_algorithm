def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]  # 해당 네모값중 하나 # 모두 같아야 통과임
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  # 한번이라도 다르면 그 네모는 압축불가
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return

        # 무사히 다 통과했다면 압축가능
        answer[init] += 1

    comp(0, 0, N)
    return answer