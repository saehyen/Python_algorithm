def solution(arr):
    # 최대공약수 = math라이브러리 내에 존재
    from math import gcd
    answer = arr[0]
    # 최대공약수를 곱할것
    for num in arr:
        answer = answer*num // gcd(answer, num)

    return answer