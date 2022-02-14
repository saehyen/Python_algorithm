map = []
answer= 0
for i in range(8):
    tmp = input()
    map.append(tmp)
for i in range(8) :
    for j in range(8) :
        if (i+j)%2 == 0 and map[i][j] == 'F':
            answer += 1
print(answer)