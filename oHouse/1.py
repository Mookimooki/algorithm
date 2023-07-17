def solution(rolls):
    scores = []    
    
    for idx, value in enumerate(rolls):
        if value == '+':
            scores.append(scores[-1] + scores[-2])
        elif value == 'R':    
            scores.remove() 
        elif value == 'D':
            scores.append(scores[-1] * 2)
        else:
            scores.append(int(value))
    
    return sum(scores)


print(solution())