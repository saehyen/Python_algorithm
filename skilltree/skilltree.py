def solution(skill, skill_trees):
    answer = 0
    while len(skill_trees) != 0:
        index = [-1] * len(skill)
        a = skill_trees.pop()
        for i in range(len(skill)):
            if skill[i] in a:
                index[i] = a.index(skill[i])
            else:
                index[i] = 9999
        c = sorted(index)
        print(index)
        if c == index:
            answer += 1
    return answer