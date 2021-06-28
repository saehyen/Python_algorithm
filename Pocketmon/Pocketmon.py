
def solution(nums):
    num_set = set(nums)

    answer = min(len(nums)/2, len(num_set))
    return answer