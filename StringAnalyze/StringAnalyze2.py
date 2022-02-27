import sys

while True:
    strings = sys.stdin.readline().rstrip('\n')
    up, lo, sp, nu = 0, 0, 0, 0

    if not strings:
        break
    for i in strings:
        if i.isupper():	# 대문자 검사
            up += 1
        elif i.islower():	# 소문자 검사
            lo += 1
        elif i.isdigit():	# 숫자 검사
            nu += 1
        elif i.isspace():	# 공백 검사
            sp += 1
    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))