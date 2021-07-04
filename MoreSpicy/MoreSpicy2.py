# heapq 사용
import heapq


def solution(scoville, k):
     heap = []
     for num in scoville:
         heapq.heappush(heap, num)

     mix_cnt = 0
     while heap[0] < k:
         try:
             heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
         except IndexError:
             return -1
         mix_cnt += 1

     return mix_cnt