def solution(s):
    s = list(s)
    answer = []
    total = 0
    # 1이 될때까지 반복
    while(len(s) != 1) :
        # 0의 개수 구하기
        answer.append(s.count("0"))
        # 1의 개수 구하기
        cnt = s.count("1")
        # 리스트로 변경
        s = list(bin(cnt))[2:]
    for item in answer :
        total += item
    return [len(answer),total]