N = int(input())
words = []
answerword = list(map(str,input()))
for i in range(N-1) :
    words.append(input())
for word in words :
    for j in range(len(word)):
        if answerword[j] != word[j] :
            answerword[j] = '?'

print(''.join(answerword))