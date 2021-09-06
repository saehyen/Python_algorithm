### DFS 풀이
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    # N : 숫자 개수
    N = len(numbers)
    # 0
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer