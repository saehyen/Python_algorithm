n = int(input())
x,y = 1,1

m = list(input().split())

for i in m :

 if i == 'R':
    y += 1
 if i == 'L':
    y -= 1
 if i == 'U':
    x -= 1
 if i == 'D':
    x += 1

 if x == 0:
     x = 1
 if x == n + 1:
     x = n
 if y == n + 1:
     y = n
 if y == 0:
     y = 1


print(m)
print(x,y)