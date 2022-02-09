price = int(input())
change = 1000-price
answer = 0
change_list = [500,100,50,10,5,1]
for i in change_list:
    if change != 0 :
        answer += (change//i)
        change = change % i
print(answer)
