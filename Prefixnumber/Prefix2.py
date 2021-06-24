from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    array = []
    prefix = True
    m = int(sys.stdin.readline())
    for j in range(m):
        queue.append(sys.stdin.readline().rstrip())
    while queue:
        a = queue.popleft()
        for l in queue:
            if a == l[:len(a)]:
                    print('No')
                    prefix = False
                    break
    if prefix == True :
        print('yes')
