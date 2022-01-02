numlist = set(range(1,10001))
answerlist = set()

for i in range(1,10001):
    for j in str(i) :
        i += int(j)
    answerlist.add(i)

self_num = sorted(numlist - answerlist)
for i in self_num:
    print(i)