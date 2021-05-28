# 우선순위 큐를 이용한 풀이
from queue import PriorityQueue
import sys
n = int(input())
q = PriorityQueue()
result = 0

for i in range(n) :
    q.put(int(sys.stdin.readline()))

while q.qsize() >= 2:
    a = q.get()
    b = q.get()
    result += a+b
    q.put(a+b)

print(result)