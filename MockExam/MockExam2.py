def solution(answers):
    counts = [0, 0, 0]
    winner = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ]

    for i in range(len(answers)):
        if answers[i] == s1[(i % 5)]:
            counts[0] += 1
        if answers[i] == s2[(i % 8)]:
            counts[1] += 1
        if answers[i] == s3[(i % 10)]:
            counts[2] += 1

    for i in range(3):
        if counts[i] == max(counts):
            winner.append(i + 1)

    return winner