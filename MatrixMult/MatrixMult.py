# 넘파이로 변환시킨다음 리스트로 리턴
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));