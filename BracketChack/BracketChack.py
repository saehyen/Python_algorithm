def solution(s):
    stack = []
    answer = True
    for i in s :
        if i == "(" :
            stack.append("(");
        else :
            if len(stack) < 1 :
                return False
            elif stack[-1] == "(" :
                stack.pop()
            else :
                answer = False
    if len(stack) >= 1 :
        return False
    return answer