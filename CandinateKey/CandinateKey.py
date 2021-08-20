from itertools import combinations


def solution(relation):
    answer = 0

    temp = [i for i in range(len(relation[0]))]
    combi_lists = []

    # 조합 생성
    for cnt in range(1, len(relation[0]) + 1):
        combi_lists.append(list(combinations(temp, cnt)))
    # combi_lists = 조합
    # 조합리스트를 문자열로 변경
    # 0, 형식을 str로 변형 -> , 처리
    combi_str_list = []
    for combi_list in combi_lists:
        for i in combi_list:
            combi_str_list.append(''.join(map(str, i)))
    # combi_str_list : 가능한조합(str형태)

    while len(combi_str_list) > 0:
        candidate_key = list()
        is_candidate_key = True

        for r in relation:
            key = ""
            for j in combi_str_list[0]:
                key += r[int(j)]

            if key in candidate_key:
                is_candidate_key = False
                break
            else:
                candidate_key.append(key)

        if is_candidate_key is False:
            del combi_str_list[0]
            continue

        str_list = list(combi_str_list[0])
        # 희소성 처리
        combi_str_list = [s for s in combi_str_list if any(str not in s for str in str_list)]

        answer += 1

    return answer