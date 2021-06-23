def solution(nums):
    result = 0

    # 3가지 고르는 함수
    a, b, c = 0, 0, 0
    for i in range(0, len(nums) - 2):
        a = nums[i]
        for j in range(i + 1, len(nums) - 1):
            b = nums[j]
            for k in range(j + 1, len(nums)):
                c = nums[k]
                d = a + b + c
                Flag = True
                for f in range(2, d):
                    # 만약 소수가 아니라면
                    if d % f == 0:
                        Flag = False
                if Flag == True:
                    result += 1
    return result