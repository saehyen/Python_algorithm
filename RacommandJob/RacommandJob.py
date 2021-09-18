def solution(table, languages, preference):
    newtable =[]
    score = [0] * len(table)
    for ta in table :
        newtable.append(ta.split())
    
    #1 사용 언어 별 직업군 점수 구하기
    for lang, pre in zip(languages,preference) :
        for i in range(len(table)) :
            if lang in table[i] :
                score[i] += (6 - newtable[i].index(lang))*pre 
    
    pos = [newtable[i][0] for i in range(len(newtable))] # pos = 직업군 목록(이름)이 담긴 리스트
    
    #2 pos 정렬, 정렬 기준 1순위 - 총점 내림차순, 2순위 - 직업군 이름 오름차순 
    sortedPos = sorted(dict(zip(pos, score)).items(), key = lambda x: (-x[1], x[0]))
    
    # answer = 가장 높은 총점 & 이름이 사전 순으로 앞에 오는 직업군
    answer = sortedPos[0][0]
    
    return answer
        
        