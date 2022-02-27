import sys
while True:
    strings = sys.stdin.readlines.rstrip('\n')
    a,b,c,d = 0,0,0,0

    if not strings:
        break
    for i in strings :
        if i.isupper():
            a += 1
        elif i.islower():
            b += 1
        elif i.isdigit():
            c += 1
        elif i.isspace():
            d += 1
    print(a,b,c,d)