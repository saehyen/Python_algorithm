A,B = map(int,input().split())

mA = str(A).replace('5','6')
mB = str(B).replace('5','6')
maxAns = int(mA) + int(mB)

nA = str(A).replace('6','5')
nB = str(B).replace('6','5')
minAns = int(nA) + int(nB)
print(minAns,maxAns)