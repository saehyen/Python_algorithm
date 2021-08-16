def grade(score):
    gra = "F"

    if score >= 90:
        gra = "A"
    elif 80 <= score < 90:
        gra = "B"
    elif 70 <= score < 80:
        gra = "C"
    elif 50 <= score < 70:
        gra = "D"
    return gra


def solution(scores):
    answer = ""
    scoreavg = []
    scores_ = [[0] * len(scores) for i in range(len(scores))]
    array = [[0] * 11 for i in range(10)]
    # 뒤집기
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores_[i][j] = scores[j][i]
    # 정렬
    for i in range(len(scores_)):
        scores_[i].sort()
    # 계산
    for i in range(len(scores_)):
        scoresum = sum(scores_[i])
        scorelen = len(scores)
        if max(scores_[i]) == scores[i][i] and max(scores_[i]) != scores_[i][scorelen - 2]:
            scoresum -= scores[i][i]
            scorelen -= 1
            print(scores[i][i])
        elif min(scores_[i]) == scores[i][i] and min(scores_[i]) != scores_[i][1]:
            scoresum -= scores[i][i]
            scorelen -= 1
            print(scores[i][i])

        answer += grade(scoresum / scorelen)
    return answer