import heapq
import sys

N, K = map(int, input().split())
gem = []
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])

bag = []
for _ in range(K):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)

total_value = 0  # 답이 될 숫자
capable_gem = []  # 현재 bag의 capacity보다 작은 모든 보석들

for _ in range(K):
    capacity = heapq.heappop(bag)  # Bag의 최솟값을 heappop 해준다. 해당 Bag은 현재의 capacity 즉, 수용량이 된다

    while gem and capacity >= gem[0][0]:  # 현재 bag의 capacity보다 이하인 모든 보석에 관하여
        [weight, value] = heapq.heappop(gem)  # 최소 무게부터 차례대로 꺼낸다
        heapq.heappush(capable_gem, -value)  # 무게를 제외한 값만 heappush하여 넣어준다(최대힙 구성)

    if capable_gem:  # gem 최소보다는 작지만 넣을 수 있는 보석들은 있는 경우
        total_value -= heapq.heappop(capable_gem)
    elif not gem:  # 남은 보석이 한 개도 없는 경우
        break

print(total_value)