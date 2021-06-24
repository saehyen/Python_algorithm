def solution(s):
    stack = []
    for i in s:
        # 스택이 비었으면 1개 추가
        if len(stack) == 0:
            stack.append(i)
        # 스택 맨위의 값이 i와 같다면 pop
        elif stack[-1] == i:
            stack.pop()
        # 같지 않다면 스택에 1개 추가
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else: return 0