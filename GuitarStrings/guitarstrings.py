N,M = map(int,input().split())
a_list = []
b_list = []
for i in range(M):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)
a_min = min(a_list)
b_min = min(b_list)

print(min(a_min*(N//6) + b_min*(N%6),a_min*(N//6 + 1),b_min*N))
