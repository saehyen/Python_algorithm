from collections import deque
import sys
n = int(input())

for i in range(n):
    array = []
    prefix = True
    m = int( sys.stdin.readline())
    for j in range(m):
        array.append(sys.stdin.readline().rstrip())
    array.sort(key=lambda x:-len(array))
    queue = deque(array)

    while queue:
        a = queue.popleft()
        for l in queue:
            if a == l[:len(a)]:
                    print('No')
                    prefix = False
                    break
    if prefix == True :
        print('yes')
