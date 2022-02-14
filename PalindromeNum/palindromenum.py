n = 1
numbers = []
answer = []
while (n != 0):
    n = int(input())
    numbers.append(n)
for i in numbers :
    if list(str(i)) == list(str(i))[::-1]:
        answer.append("Yes")
    else :
        answer.append("No")
for ans in answer[:-1] :
    print(ans)