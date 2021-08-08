#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    babo = set(lost) & set(reserve)
    reserve = list(set(reserve) - babo)
    lost = sorted(list(set(lost) - babo))
    
    for x in lost:
        for y in [x-1, x+1]:
            if y in reserve:
                reserve.remove(y)
                n += 1
                break
    
    return n - len(lost)

print(solution(5, [2, 3, 4], [5, 3, 4]))