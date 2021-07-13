# 최소값과 최대값을 구하는 문제
# 간단하게 return하는 방법 구현
def solution(s):
    x = list(map(int, s.split()))
    return str(min(x)) + " " + str(max(x))