n, m = map(int, input().split())
# 세로가 1이라면 시작만
if n == 1:
    print(1)
# 세로가 2라면 선택권은 2번3번만 존재
elif n == 2:
    print(min(4, (m-1)//2+1))
# 가로의 길이가 6이하일 경우 최대값은 4, 최소값은 가로길이
elif m <= 6:
    print(min(4, m))
# 오른쪽으로 두칸을 가는 강제적인 방법을 제외하면 한칸만 움직이면 됨
else:
    print(m-2)