heightlist = []
for _ in range(9) :
    heightlist.append(int(input()))
total = sum(heightlist)
for i in range(9) :
    for j in range(i+1,9) :
        if (total - heightlist[i] - heightlist[j]) == 100 :
            first = heightlist[i]
            second = heightlist[j]
            break
heightlist.remove(first)
heightlist.remove(second)
for _ in sorted(heightlist) :
    print(_)