N = int(input())
amin, amax, bmin , bmax ,S = 1000000000000000,0,0,0,0
answerlist = []
ans = 0
for _ in range(N) :
    a, b = map(int, input().split())
    answerlist.append([a,b])
    # 만약 a가 amin보다 작거나 같고, 가치는 크거나 같을시
    # 최대값 변경
    if a >= amax and b-a>= bmax-amax and amin<a: 
        amax = a
        bmax = b
        print("최대값 변경 : ", a)
    # 만약 a가 amin보다 작거나 같고, 가치는 크거나 같을시
    # 최소값 변경
    if a <= amin and b-a>= bmin-amin : 
        amin = a
        bmin = b
        print("최소값 변경 : ", a)
    
# 조건에 맞는 정답들 더해서 출력
for answer in answerlist:
    if answer[0] >= amin and answer[0] <= amax:
        ans += answer[1]
ans = ans + bmin + bmax - amax + amin
print("답 : ",ans, "최대값 : ", amax , "최소값 : ", amin)