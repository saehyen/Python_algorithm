n = int(input ())
A = list (map (int, input ().split ()))
B = list (map (int, input ().split ()))

answer = 0;
# A의 최대값과 B의 최솟값을 곱한값을 더하는 방식
for i in range(n):
    answer += min(B) * max(A);
    A.remove(max(A));
    B.remove(min(B));

print(answer);
