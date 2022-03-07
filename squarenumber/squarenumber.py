n = int(input())
m = 1
answer = 0
while n != 0:
    if m**2 <= n :
        m += 1
    else :
        n -= ((m-1)**2)
        answer+=1
        m=1
print(answer)