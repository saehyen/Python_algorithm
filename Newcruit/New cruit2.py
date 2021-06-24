n = int(input())
scorelist1 = []
scorelist2 = []
index1 = []
index2 = []
num = 0
for i in range(0, n):
    m = int(input())
    for l in range(0, m):
        k, j = input().split()
        scorelist1.append([k, j])
        scorelist2.append([k,j])
    scorelist1.sort()
    scorelist2.sort(key=lambda x: x[1])

    for i in scorelist1:
        index = scorelist1.index(i)
        index1.append(index)
        index = scorelist2.index(i)
        index2.append(index)

        maxindex = min(m-index1[num] , m-index2[num])
        num += 1
    num = 0
    print(maxindex)
    maxindex = 0