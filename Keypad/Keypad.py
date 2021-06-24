def solution(numbers, hand):
    lefthand = [1, 4, 7, 10]
    righthand = [3, 6, 9, 12]
    selecthand = [2, 5, 8, 0]
    son = hand.split()
    if 'right' in son:
        son = True
    else:
        son = False

    left = '10'
    right = '12'
    result = []
    for i in numbers:
        if i == 0:
            i = 11

    for number in numbers:
        if number in lefthand:
            result.append('L')
            left = number
        elif number in righthand:
            result.append('R')
            right = number
        # 중간 번호를 입력하게 된다면.
        elif number in selecthand:
            # 오른손잡이일경우
            if hand == right:
                result.append('T')
                # 그 손 그대로 누르면 되는 경우
                if (number - right) == 0:
                    result.append('R')
                    right = number
                elif (number - left) == 0:
                    result.append('L')
                    left = number
                # 1칸 차이인 경우
                elif abs(number - right) == 1 or abs(number - right) == 3:
                    result.append('R')
                    right = number
                elif abs(number - left) == 1 or abs(number - left) == 3:
                    result.append('L')
                    left = number
                # 2칸 차이인 경우
                elif abs(number - right) == 6 or abs(number - right) == 2 or abs(number - right) == 4:
                    result.append('R')
                    right = number
                elif abs(number - left) == 6 or abs(number - left) == 2 or abs(number - left) == 4:
                    result.append('L')
                    left = number
                # 3칸 차이인 경우
                elif abs(number - right) == 7 or abs(number - right) == 5:
                    result.append('R')
                    right = number
                elif abs(number - left) == 7 or abs(number - left) == 5:
                    result.append('L')
                    left = number
                # 4칸 차이인 경우
                elif abs(number - right) == 8:
                    result.append('R')
                    right = number
                elif abs(number - left) == 8:
                    result.append('L')
                    left = number
            # 왼손잡이인 경우
            if hand == left:
                # 중간번호를 누를 경우
                if number in selecthand:
                    # 그 손 그대로 누르면 되는 경우
                    if (number - left) == 0:
                        result.append('L')
                        left = number
                    elif (number - right) == 0:
                        result.append('R')
                        right = number

                    # 1칸 차이인 경우
                    elif abs(number - left) == 1 or abs(number - left) == 3:
                        result.append('L')
                        left = number
                    elif abs(number - right) == 1 or abs(number - right) == 3:
                        result.append('R')
                        right = number
                    # 2칸 차이인 경우
                    elif abs(number - left) == 6 or abs(number - left) == 2 or abs(number - left) == 4:
                        result.append('L')
                        left = number
                    elif abs(number - right) == 6 or abs(number - right) == 2 or abs(number - right) == 4:
                        result.append('R')
                        right = number

                    # 3칸 차이인 경우
                    elif abs(number - left) == 7 or abs(number - left) == 5:
                        result.append('L')
                        left = number
                    elif abs(number - right) == 7 or abs(number - right) == 5:
                        result.append('R')
                        right = number
                    # 4칸 차이인 경우
                    elif abs(number - left) == 8:
                        result.append('L')
                        left = number
                    elif abs(number - right) == 8:
                        result.append('R')
                        right = number
    answer = ''
    for i in result:
        answer += i
    return answer