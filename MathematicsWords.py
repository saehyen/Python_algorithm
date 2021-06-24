# 숫자 입력받기
N = int(input())
# 단어 리스트
words = []
for i in range(N) :
  words.append(input())

# 딕셔너리 초기화
dict = {}
# 자리수 구해서 숫자값과 연결시킴.
for word in words :
    k = len(word) -1
    for s in word :
        if s in dict :
            dict[s] += pow(10,k)
        else :
            dict[s] = pow(10,k)
        k-=1

    nums=[]

    for value in dict.values():
        nums.append(value)
    # 내림차순 정렬
    nums.sort(reverse=True)
    # 결과값 초기화 및 9부터 입력
    result = 0
    t = 9

    # 최대값부터 result에 저장
    for i in range(len(nums)) :
        result += nums[i] * t
        t -= 1

print(result)

