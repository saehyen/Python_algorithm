n = int(input())
scorelist = []
num = 0
resultlist = []
result = 0

for i in range (0,n) :
    m = int(input())
    for l in range (0,m) :
        k,j = input().split()
        scorelist.append([k, j])
    # 정렬
    scorelist.sort()
    # 비교
    for i in scorelist :
        for k in range(num, m) :
            if i[1] > scorelist[num][1] :
                num += 1
            else :
                break
            result += 1

    resultlist.append(result)
    result = 0
for i in resultlist :
    print(i)