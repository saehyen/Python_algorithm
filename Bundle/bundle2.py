# 힙을 이용한 풀이
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

result = 0

while len(heap) != 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    _sum = num1 + num2
    result += _sum
    heapq.heappush(heap, _sum)

print(result)