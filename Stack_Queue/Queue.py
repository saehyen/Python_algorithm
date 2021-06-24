def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

test1 = [93, 30, 55]
speed1 = [1,30,5 ]
test2 = [95, 90, 99, 99, 80, 99]
speed2 = [1,1,1,1,1,1]
print(solution(test1,speed1))
print(solution(test2,speed2))