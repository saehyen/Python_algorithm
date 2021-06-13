import sys; input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    answer = list(map(int, input().split())) + list(map(int, input().split()))
    print(' '.join(map(str, sorted(answer))))

solution()