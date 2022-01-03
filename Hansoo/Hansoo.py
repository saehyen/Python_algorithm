N = int(input())
ans = 99
if N < 100 :
    print(N)
else :
    for i in range(100,N+1) :
        if (int(str(i)[2]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[0])) :
            ans += 1
        else:
            continue
    print(ans) 