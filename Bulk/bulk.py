N = int(input())
bulklist = []
answerlist = []
cnt = 0
for i in range(N):
    a,b = map(int,input().split())
    bulklist.append([a,b])

for i in range(N):
    count = 0
    for j in range(N):
        if bulklist[i][0] < bulklist[j][0] and bulklist[i][1] < bulklist[j][1]: 
            count += 1 
    answerlist.append(count + 1) 
 
for d in answerlist:
    print(d,end=" ")
