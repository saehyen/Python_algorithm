from itertools import combinations
from collections import defaultdict

def solution(infos, querys):
    answer = []
    # 딕셔너리 초기화
    info_dict = defaultdict(list)
    # 각각의 요소 딕셔너리에 넣기 (마지막값은 score)
    for info in infos:
        temp = info.split(" ")
        key = temp[0:-1]
        score = int(temp[-1])
        # 가능한 조합 경우의수 집어넣기
        for i in range(5):
            combi = list(combinations(key, i))
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)
    # 키값순으로 정렬
    for key in info_dict.keys():
        info_dict[key].sort()
    # 쿼리값 정리
    for query in querys:
        query = query.split(" ")
        query_score = int(query[-1])
        query_key = query[:-1]
        # and 제거
        for _ in range(3):
            query_key.remove("and")
        # '-' 제거
        while "-" in query_key:
            query_key.remove("-")
        query_key = ''.join(query_key)
        # 경우의 수가 존재하면
        if query_key in info_dict:
            scoreList = info_dict[query_key]
            # 스코어 비교 ( 이진 탐색 )
            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= query_score:
                        right = mid
                    else:
                        left = mid+1
                answer.append(len(scoreList)-left)
        # 경우의 수가 없다면 0 추가
        else:
            answer.append(0)

    return answer