e,s,m = map(int,input().split())
answer = s
if e == 15 :
    e = 0
if s == 28 :
    s = 0
if m == 19 :
    m = 0
while True:
    if answer%15 == e and answer%19 == m :
        break
    else:
        answer += 28
print(answer)