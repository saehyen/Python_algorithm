N = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = 0
for i in range(N):
    # 범위를 미리 지정
    tmp = arr[:i] + arr[i + 1:]
    # start, end 포인터 지정
    left, right = 0, len(tmp) - 1
    while left < right:  # 사이 값일 경우
        t = tmp[left] + tmp[right] # 합계는 t 
        if t == arr[i]: # t와 arr값이 같다면
            ans += 1
            break
        if t < arr[i]: left += 1 # t 를 증가시켜야 하므로 left 증가
        else: right -= 1 # t 를 감소시켜야 하므로 right 감소
print(ans)