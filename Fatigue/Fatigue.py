from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 순열 조합따라 condition에 넣기
    for condition in permutations([i for i in range(len(dungeons))]):
        kTemp, ansTemp = k, 0
        
        for index in condition:
            minimumRequired, consumption = dungeons[index]
            #최소 피로도 조건 충족시
            if kTemp >= minimumRequired:
                # 피로도 소비 및 ansTemp + 1
                kTemp -= consumption
                ansTemp += 1
                
        # 가장 큰 정답값 return
        answer = max(answer, ansTemp)

    return answer