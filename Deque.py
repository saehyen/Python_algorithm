from collections import deque
def solution(progresses, speeds):
    answer = []
    sum = 0
    progresses = deque(progresses)
    # progresses 원소가 빌 때까지
    while progresses:
        # 각 원소에 speed 만큼 더해줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 100이 넘는 원소가 끝날때까지 pop:
        while progresses:
            a = progresses.popleft()
            if a >= 100:
                sum += 1
            else :
                progresses.appendleft(a)
                break
        if sum != 0 :
            answer.append(sum)
            sum = 0
    return answer


test1 = [93, 30, 55]
speed1 = [1,30,5 ]
test2 = [95, 90, 99, 99, 80, 99]
speed2 = [1,1,1,1,1,1]
print(solution(test1,speed1))
print(solution(test2,speed2))