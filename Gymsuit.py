def solution(n, lost, reserve):
    result = n
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    lost = set_lost
    reserve = set_reserve

    for lo in lost:
        if lo - 1 in reserve:
            reserve.remove(lo - 1)
        elif lo + 1 in reserve:
            reserve.remove(lo + 1)
        else:
            result -= 1
    return result