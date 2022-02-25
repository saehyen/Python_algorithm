n = int(input())
word = list(map(str,input()))
stack = ['*']
i = 0 
while i != n :
    if word[i] == 'L' :
        i += 2
        stack.append('LL')
        stack.append('*')
    else :
        i += 1
        stack.append('S')
        stack.append('*')
print(min(n,stack.count('*')))