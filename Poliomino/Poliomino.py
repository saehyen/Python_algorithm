board = input()
# 4개를 먼저 바꾸고
board = board.replace("XXXX", "AAAA")
# 2개를 바꿈
board = board.replace("XX", "BB")
# X가 존재한다면 -1 출력
if 'X' in board:
    print(-1) 
# 아니라면 그대로 출력
else: 
    print(board)
