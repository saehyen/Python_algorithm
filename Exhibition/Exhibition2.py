N = int(input())
amin, amax, bmin , bmax ,S = 1000000000000000,0,0,0,0
answerlist = []
ans = 0
# 리스트 입력 및 정렬
for _ in range(N) :
    a, b = map(int, input().split())
    answerlist.append([a,b])
answerlist.sort()
amin = answerlist[0][0]
bmin = answerlist[0][1]
amax = answerlist[1][0]
bmax = answerlist[1][1]



print(answerlist)
# 정렬시킨 리스트 후처리
