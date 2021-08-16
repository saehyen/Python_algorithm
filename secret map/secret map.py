def solution(n, arr1, arr2):
    answer = []
    # arr1 = i, arr2 = j
    for i, j in zip(arr1, arr2):
        # 2진수의 문자로 변경 ( bin )

        a12 = str(bin(i | j)[2:])
        print(a12)
        # 파이썬의 내장함수
        # rjust = 공백을 채워주는 함수
        a12 = a12.rjust(n, '0')
        # 1은 #으로
        a12 = a12.replace('1', '#')
        # 0 은 공백
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer