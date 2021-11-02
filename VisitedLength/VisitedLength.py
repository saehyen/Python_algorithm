def solution(dirs):
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    d = {"U": 0, "L":1, "D":2, "R": 3}
    # set자료형으로 선언하여 중복없애기
    visited = set()
    answer = 0
    # 초기 좌표 설정
    x, y = 0, 0
    # 좌표 이동 설정
    for dir in dirs:
        i = d[dir]
        nx, ny = x + dxs[i], y + dys[i]
        # 벽 만날시 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        # 방문하지 않았다면
        if (x, y, nx, ny) not in visited:
            # 이동전 좌표와 이동 후 좌표 설정
            visited.add((x, y, nx, ny))
            # 길은 양쪽에서 가능
            visited.add((nx, ny, x, y))
            # 갔던 길이 아니라면 +1
            answer += 1
        # 이동한 뒤 좌표 설정
        x, y = nx, ny

    return answer