x = input()
x = list(map(int,x))
sum = 0
x.sort(reverse=True)
for i in x:
    sum += i
if x[len(x)-1] != 0 :
    print(-1)
elif sum % 3 == 0 :
    for i in x:
        print(i,end='')
else :
    print(-1)