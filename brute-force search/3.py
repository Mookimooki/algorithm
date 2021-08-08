def solution(brown, yellow):
    brown = [(x, (brown + 4) // 2 - x) for x in range(3, (brown + 8) // 4)]
    
    for x, y in brown:
        if (x - 2) * (y - 2) == yellow:
            return [y, x]

print(solution(24, 24))
