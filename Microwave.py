t = int(input())

if (t % 10)!= 0 :
    print('-1')
    exit(0)

A = int(t / 300)
B = int ((t - (A * 300)) / 60)
C = int((t-(A*300)-(B*60)) / 10)

print(A, B, C)