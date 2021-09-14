def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    enter_idx = 0
    leave_idx = 0
    room = set()
    # 모든사람이 떠날때까지 반복
    while leave_idx < n:
        # 방에 사람이 있으면 나가게하고 leave_idx +1
        if leave[leave_idx] in room:
            room.discard(leave[leave_idx])
            leave_idx += 1
            continue
        # 방에 사람이 없으면
        if enter[enter_idx] not in room:
            # 만나는 사람 추가
            for man in room:
                answer[man] += 1
            # 남아있는 사람수만큼 answer에 기록
            answer[enter[enter_idx]] = len(room)
            room.add(enter[enter_idx])
            # 들어오는 사람 인덱스 + 1
            enter_idx += 1
    return answer[1:]