n = int(input())
m = int(input())

vip = []
# vip 자리 확정
for i in range(0,m):
    k = int(input())
    vip.append(k)
# 점화식 a0 = 1 a1=1 a2=2 , sit[i-2]+sit[i-1]
sit = [1,1,2]

# DP 테이블 구성
for i in range(3,41):
    sit.append(sit[i-2]+sit[i-1])
ans = 1
# 점화식 내부 규칙 적용
if m >= 1:
    pre = 0
    # 구간설정하여 ans에 곱해주기
    for i in range(0,m):
        ans = ans * sit[vip[i]-1-pre]
        pre = vip[i]
    ans = ans * sit[n-pre]
else:
    # 1이하인 경우까지 계산
    ans = sit[n]
# 결과값 출력
print(ans)