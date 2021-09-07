# 문제를 잘못 이해한 답
def solution(orders, course):
    # 문자열 합집합 구하기
    answer = []
    answer2 = []
    for i in range(0,len(orders)) :
        for j in range(i+1,len(orders)) :
            union = list(set(orders[i]) & set(orders[j]))
            union.sort()
            if len(union) >= 2 :
                answer.append("".join(union))
    
    answer = list(set(answer))
    # 코스에 포함된 리스트 개수인것만 result_list
    for co in course :
        for an in answer :
            if len(an) == co :
                answer2.append(an)
    
    # 오름차순 정렬 후 리턴
    answer2.sort()
    return answer2
    
    