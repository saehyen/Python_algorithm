def solution(brown, yellow):
    size = brown + yellow
    x = []
    for i in range(1,size+1) :
        if size%i == 0 and i != 1:
            x.append(i)
    x.sort(reverse=True)
    for i in x :
        a = i
        for j in x :
            b = j
            if (a-2) * (b-2) == yellow :
                return [a,b]