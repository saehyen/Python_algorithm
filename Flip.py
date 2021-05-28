S = input()
count1 = 0
count2 = 0

while len(S) != 0 :
    if S[0] == '0' :
        S = S.lstrip('0')
        count1 += 1

    elif S[0] == '1' :
        S = S.lstrip('1')
        count2 += 1

print(min(count1,count2))