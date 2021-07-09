def solution(name):
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    pos = 0
    answer = 0
    while True:
        answer += moves[pos]
        moves[pos] = 0

        if sum(moves) == 0: break

        left = 1
        right = 1
        # 방향마다의 거리 구하기
        while moves[pos - left] == 0:
            left += 1

        while moves[pos + right] == 0:
            right += 1

        if left >= right:
            pos += right
            answer += right

        else:
            pos -= left
            answer += left

    return answer
