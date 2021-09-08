def solution(info, query):
    answer = [0 for x in range(len(query))]
    querylist = []
    infolist = []
    # 쿼리문 정리
    for i in range(len(query)):
        test = query[i].split()
        while ('and' in test) :
            test.remove('and')
        querylist.append(test)
        #print(test)
        
    # info문 작업
    for j in info :
        t = j.split()
        infolist.append(t)
        
    # 쿼리문,정보 비교
    for i in range(len(infolist)):
        for j in range(len(querylist)):
            flag = 0
            for k in range(4):
                if infolist[i][k] != querylist[j][k]:
                    if querylist[j][k] != '-':
                        flag = 1
                        break
            if flag == 0:
                if int(infolist[i][4]) >= int(querylist[j][4]):
                    answer[j] += 1
    return answer
                