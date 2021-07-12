from collections import deque
def solution(people, limit):
    people.sort()
    people=deque(people)
    count = 0

    while people :
        # x = 제일 큰수 y = 제일 작은수
        x = people.pop()
        y = people.popleft()
        if x + y <= limit :
            count += 1
        elif x+y > limit:
            people.appendleft(y)
            count += 1
        if len(people) == 1 :
            people.pop()
            count +=1
            break
    return count