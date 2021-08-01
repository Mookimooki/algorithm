def solution(progresses, speeds):
    answer = []
    merged = [[progress + speed, speed] for progress, speed in zip(progresses, speeds)]
    
    while len(merged) > 0:
        while(merged[0][0] < 100):
            merged = [[progress + speed, speed] for progress, speed in merged]
        answer.append(0)
        while(len(merged) > 0 and merged[0][0]>= 100):
            answer[-1] = answer[-1] + 1
            del merged[0]
        
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))