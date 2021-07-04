# 정답(시간초과)
from collections import deque
def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville=deque(scoville)
    while K > min(scoville):
        scoville = deque(sorted(list(scoville)))
        answer += 1
        if len(scoville) == 1 and min(scoville) < K :
            return -1
        a = scoville.popleft()
        b = scoville.popleft()
        c = a+b*2
        scoville.appendleft(c)
    return answer