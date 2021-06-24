N = int(input())
cnt = 1
timelist = []
for i in range (0,N) :
    start_time, end_time = map(int,input().split())
    timelist.append([start_time,end_time])
# 2번째 인자를 기준으로 정렬

timelist.sort(key=lambda x:(x[1],x[0]))
select_time = timelist[0][1]

if timelist[0][1] == timelist[0][0]:
    cnt -= 1
for i in timelist :
    if select_time <= i[0] :
        cnt += 1
        select_time = i[1]

print(cnt)
