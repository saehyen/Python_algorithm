# senumerate를 사용한 정답
def solution(s):
    new_s = s.split(' ')
    answer = ''
    for word in new_s:
        for i, spell in enumerate(word):
            answer += spell.upper() if i % 2 == 0 else spell.lower()
        answer += ' '
    return answer[:-1]