def solution(s):
    LENGTH = len(s)
    STR, COUNT = 0, 1
    cand = [LENGTH]  # 1~len까지 압축했을때 길이 값

    for size in range(1, LENGTH):
        compressed = ""
        # string 갯수 단위로 쪼개기 *
        splited = [s[i:i+size] for i in range(0, LENGTH, size)]
        stack = [[splited[0], 1]]

        for unit in splited[1:]:
            if stack[-1][STR] != unit:  # 이전 문자와 다르다면
                stack.append([unit, 1])
            else:  # 이전 문자와 다르다면
                stack[-1][COUNT] += 1

        compressed += ('').join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
        cand.append(len(compressed))

    return min(cand)  # 최솟값 리턴