word = str(input())
answer = []
for i in range(1,len(word)):
    answer.append(word[i:])
answer.sort()
for i in answer :
    print(i)