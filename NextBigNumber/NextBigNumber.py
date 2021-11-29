def solution(n):
    # 2진수로 바꾸기
    n_ = str(bin(n))[2:]
    # 1밖에 없다면 10붙이기
    if len(set(n_)) == 1 :
        return int('10' + n_[1:],2)
    # 1의 개수
    cnt = n_.count('1')

    while(True):
        # 1씩 커지면서 테스트
        n += 1
        # 1의 개수가 같다면 리턴
        if str(bin(n))[2:].count('1') == cnt : 
            return n