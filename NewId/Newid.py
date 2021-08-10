def solution(new_id):
    # step 1
    answer = ''
    new_id = new_id.lower()

    # step 2
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    # step 3
    while '..' in answer:
        answer = answer.replace('..','.')
    #step4
    answer = answer.rstrip('.')
    answer = answer.lstrip('.')

    #step5
    if len(answer) < 1 :
        answer += "a"

    #step6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.' :
            answer = answer.rstrip('.')
    # step7
    if len(answer) <= 2 :
        while(len(answer) < 3) :
            answer = answer + answer[-1]
    return answer
