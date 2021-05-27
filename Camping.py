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

    while V != 0 :
        for i in range(0,L) :
            if V == 0 :
                break
            result += 1
            V -= 1

        for i in range(0,T) :
            if V == 0 :
                break
            V -= 1
    result_list.append(result)

    result = 0
