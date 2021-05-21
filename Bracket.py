n = list(input().split('-'))
result = 0
#첫번째 값과 이후 값 분리
firstlist = n[:1]
res_list =n[1:]


#첫번째 식 처리 ( 더할 값 )
for i in firstlist :
    l = i.split('+')
    # 문자열로 된 식 int 값으로 변경(map)
    l = map(int,l)
    # lstrip 은 앞에 있는 문자열 제거
    first_i = i.lstrip('0')
    for t in l :
        result += t
#두번째 이후 식 처리 ( 뺄 값 )
for i in res_list :
    l = i.split('+')
    # 문자열로 된 식 int 값으로 변경(map)
    l = map(int, l)
    # lstrip 은 앞에 있는 문자열 제거
    first_i = i.lstrip('0')
    for t in l:
        result -= t

print(result)
