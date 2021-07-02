def solution(clothes):
    clothes = sorted(clothes,key=lambda x:x[1])
    sut = [0] * 30
    sut[0] = 1
    j = 0
    for i in range(len(clothes)-1) :
        if clothes[i][1] != clothes[i+1][1] :
            j += 1
        sut[j] += 1
    xsum = 1
    ysum = 1
    while 0 in sut :
        sut.remove(0)
    # 각 옷 종류별 개수로 연산하기
    for i in range(0,len(sut)) :
        ysum *= (sut[i]+1)
    return ysum-1