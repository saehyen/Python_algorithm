# 2021 채용연계형 인턴쉽 문제
# replace 활용
def solution(s):
    a = ["0","1","2","3","4","5","6","7","8","9"]
    b = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(10):
        s = s.replace(b[i],a[i])
    return int(s)