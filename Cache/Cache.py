def solution(cacheSize, cities):
    # 대문자로 변경
    cities = [c.upper() for c in cities]
    cache = []
    answer = 0
    # 캐시사이즈가 0인 경우
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            # 캐시안에 없다면
            if not city in cache:
                # 캐시사이즈가 도시길이보다 크다면
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                # 캐시사이즈가 도시길이보다 작다면
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            # 캐시안에 도시가 존재하는 경우
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
    
    return answer