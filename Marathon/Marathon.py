# 시간초과
def solution(participant, completion):
    while completion :
        for part in participant :
            if part in completion:
                participant.remove(part)
                completion.remove(part)
    return participant[0]