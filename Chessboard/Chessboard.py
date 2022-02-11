
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())
answer = 32

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W +=1
                    if board[k][l] != 'B':
                        first_B += 1
                else:
                    if board[k][l] != 'B':
                        first_W += 1
                    if board[k][l] != 'W':
                        first_B += 1
        answer = min(first_B,first_W,answer)
print(answer)