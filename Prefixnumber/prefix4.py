# zip,startswith 을 이용한 풀이
def solution(phoneBook):
    # 정렬
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False

    return True