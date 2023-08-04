#https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times, answer):   
    i, mins = 1, 0
    length = len(times)
    
    while mins < answer:
        mins += times[i]
        
    return answer

print(solution(6, [7, 10]), 28)