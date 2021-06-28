# try-except를 사용한 풀이
def solution(s):
    try:
        s = list(map(int, s))
    except:
        return False

    if len(s) == 6 or len(s) == 4:
        answer = True
    else:
        answer = False
    return answer