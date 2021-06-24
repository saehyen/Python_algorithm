import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

negative=[]
positive=[]
ans=0
for num in nums:
    if num<=0:      #0도 negative의 원소로 둔다.
        negative.append(num)
    elif num==1:
        ans+=1      #숫자가 1인 경우에는 묶지 않으므로, 미리 계산하여 둔다.
    elif num>1:
        positive.append(num)

# 목적에 맞게 정렬
negative.sort()
positive.sort(reverse=True)

# 1) 작은 수부터 차례대로 묶는다.
for i in range(0,len(negative),2):
    if i+1 < len(negative):
        ans += negative[i]*negative[i+1]
    else:
        ans += negative[i]

# 2) 큰 수부터 차례대로 묶는다.
for i in range(0,len(positive),2):
    if i+1 < len(positive):
        ans += positive[i]*positive[i+1]
    else:
        ans += positive[i]

print(ans)