def getMax(n):
    max = [1 for i in range(n//2)]
    if n&1: max[0]=7
    return max

def getMin(n):
    ret = [8 for i in range((n+6)//7)]
    if n%7==1: ret[0]=1; ret[1]=0
    if n%7==2: ret[0]=1
    if n%7==3: ret[0]=2; ret[1]=0; ret[2]=0
    if n%7==4: ret[0]=2; ret[1]=0
    if n%7==5: ret[0]=2
    if n%7==6: ret[0]=6
    return ret

n = int(input())
numlist = []
for i in range(n):
    numlist.append(int(input()))
d = [0,0,1,7,4,2,6,8,10,18,22]
for i in numlist :
    if i < 11 :
        print(d[i],"".join(map(str,getMax(i))))
    else :
        print("".join(map(str,getMin(i))),"".join(map(str,getMax(i))))
