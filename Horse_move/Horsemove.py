# 말의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 말의 이동 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-1, 2), (-2, 1), (2, 1), (1, 2)]

# 이동 가능 확인
result = 0
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8 :
        result += 1
print(result)