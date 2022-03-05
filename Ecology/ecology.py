import sys
 
trees = {}
sum = 0
 
while True:
    name = sys.stdin.readline().strip()
    if not name:
        break
    trees.setdefault(name, 0)
    trees[name] += 1
    sum += 1
 
for name in sorted(trees.keys()):
    print('{0} {1:0.4f}'.format(name, trees[name]*100/sum))