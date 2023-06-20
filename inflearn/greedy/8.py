#https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda x:x[1])
    
    lastExit = -40000
    answer = 0
    for route in routes:
        if route[0] > lastExit:
            lastExit = route[1]
            answer = answer + 1
            
    return answer


print(solution([[-18,-13], [-20,-15], [-14,-5], [-5,-3]]))