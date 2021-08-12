def solution(board, moves):
    answer = 0
    box = []
    # 움직임
    for crain in moves:
        # 뽑기
        for i in range(len(board)):
            if board[i][crain-1] > 0:
                box.append(board[i][crain-1])
                board[i][crain-1] = 0
                # 같은지 검사하기
                if len(box) >= 2 and box[len(box)-1] == box[len(box)-2]:
                    box.pop(-1)
                    box.pop(-1)
                    answer += 2
                break

    return answer