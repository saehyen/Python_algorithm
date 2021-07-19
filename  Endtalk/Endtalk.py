def solution(n, words):
    for i in range(len(words) - 1):
        # 끝말잇기 실패
        if words[i][-1] != words[i + 1][0] or words[i + 1] in words[:i + 1]:
            return [(i + 1) % n + 1, int((i + 1) / n + 1)]
    else:
        return [0, 0]
