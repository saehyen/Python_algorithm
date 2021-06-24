from collections import deque


def solution(priorities, location):

    priorities = deque(priorities)
    # 중요도가 높은게 뒤에 있으면 꺼내서 뒤로 보낸다.
    count = 0
    answer = 1
    while True:
        if max(priorities) != priorities[0]:
            a = priorities.popleft()
            priorities.append(a)
            if location != 0:
                location -= 1
            else:
                location = len(priorities) - 1
        else:
            # 중요도가 제일 높은게 앞으로 오면 꺼낸다.
            b = priorities.popleft()
            count += 1
            if location == 0:
                answer = count
                break
            else:
                location -= 1

    return answer