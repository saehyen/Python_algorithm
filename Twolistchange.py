n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse=True) # 내림차순 정렬

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i] # swap
    else:
        break

print(sum(a))