n = int(input())
answer = []
for i in range(n):
    m = int(input())
    a = m // 25
    m = m % 25
    b = m // 10
    m = m % 10
    c = m // 5
    m = m % 5
    d = m // 1
    answer.append([str(a),str(b),str(c),str(d)])
    a,b,c,d = 0,0,0,0
for i in answer :
    print(" ".join(i))
        