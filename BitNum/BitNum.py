def solution(numbers):
    answer = []

    for number in numbers:
        # 비트수를 맞추기 위해 앞에 0을 추가하고 리스트의 형태로 만듦
        bin_number = list('0' + bin(number)[2:])
        # 0의 인덱스를 찾음
        idx = ''.join(bin_number).rfind('0')
        # 0을 1로 바꿔줌
        bin_number[idx] = '1'
        # 2의 배수가 아니라면
        if number % 2 == 1:
            # index+1번째의 값은 0으로 변경
            bin_number[idx+1] = '0'
        # int로 바꿔서 정답리스트에 추가
        answer.append(int(''.join(bin_number), 2))

    return answer