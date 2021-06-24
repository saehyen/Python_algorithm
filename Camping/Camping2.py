import sys
result = 0
result_list= []
num = 1
while True :
    L,P,V = map(int,sys.stdin.readline().split())
    T = P-L
    if L == 0 and P == 0 and V == 0:
        for i in result_list :
            print('Case', num, end='')
            print(':', i)
            num += 1
        exit(0)

    result1 = int(V / P)
    if V % P >= L :
        result = result1 * L + L
    else :
        result = result1 * L + V % P

    result_list.append(result)

    result = 0