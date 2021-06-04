def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        if array[mid] > target:
            end = mid -1
        if array[mid] < target:
            start = start+1
        return None
# N(가게의 부품 개수)입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 부품이 있는지 확인
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no', end=' ')
