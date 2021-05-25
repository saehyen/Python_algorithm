n = int(input())
num = -1
scorelist=[]
testlist = []
for i in range(0, n):
    m = int(input())
    count = 0
    for l in range(0, m):
        k, j = input().split()
        scorelist.append([k, j])
    scorelist.sort(reverse= True)
    print(scorelist)
    for i in scorelist :
        testlist.append(i[1])
    for i in scorelist :
        num += 1
        if num == m-1 :
            count += 1
            print('[i] : 마지막')
            break
        if i[1] == min(testlist[num:]) :
            print('i[] : ', i)
            print(min(testlist[num:]))
            print('num : ', num)
            count += 1
    num = -1
    print(count)
    scorelist = []