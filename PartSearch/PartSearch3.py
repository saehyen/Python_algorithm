n = int(input())
# 가게에 있는 전체 부품 번호 입력받아 집합(set) 자료형 기록
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 확인
for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')