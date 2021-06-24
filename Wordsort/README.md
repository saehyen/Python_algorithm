# Wordsort
##단어를 중복제거, 길이,알파벳 순으로 정렬하기

# 코드 간단하게 구현하기
## 개행문자를 제거해서 words리스트에 넣는 코드
- words = [sys.stdin.readline().strip() for _ in range(n)]
## set 자료형으로 바꾸고(중복제거) 길이와 알파벳순으로 sorted 사용.
- for i in sorted(set(words), key=lambda x: (len(x), x)):
