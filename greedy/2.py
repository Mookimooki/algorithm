from  copy import deepcopy

def recursive_sum(strCtn ,flag, idx, length):
    if idx >= len(flag):
        idx = idx - len(flag)
    elif idx < 0:
        idx = idx + len(flag)

    strCtn[idx] = 0
    flag[idx] += 1

    if max(strCtn) < 1 :
        return length
    if flag[idx] > 2:
        return 40

    return min(recursive_sum(deepcopy(strCtn), deepcopy(flag), idx - 1, length + 1), recursive_sum(deepcopy(strCtn), deepcopy(flag), idx + 1, length + 1))

def solution(name):
    strCtn = list(map(lambda x: min(ord(x)-65, 91-ord(x)), name))
    if min(strCtn) > 0:
        return sum(strCtn) + len(strCtn) - 1 
    return sum(strCtn) + recursive_sum(strCtn, [0]*len(name), 0, 0)

print(solution("ABAAAAABB"))