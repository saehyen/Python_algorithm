def solution(s):
    answer = []
    # 첫 {} 제거
    s = s[2:-2]
    # 숫자별로 분리
    s = s.split("},{")
    # 길이가 짧은 순으로 정렬
    s.sort(key = len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer