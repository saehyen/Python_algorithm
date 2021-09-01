def solution(board):
    # n : 세로 m : 가로
    n = len(board)
    m = len(board[0])
    # dp 선언
    dp = [[0]*m for _ in range(n)]
    # 첫번째 행, 첫번째 열 dp에 복사
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]
    # 정사각형 찾기 (min(왼쪽,위쪽,왼쪽위대각선)+1)
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    answer = 0
    # 2차원 배열중에 max값 찾기
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    # 넓이값 리턴
    return answer**2