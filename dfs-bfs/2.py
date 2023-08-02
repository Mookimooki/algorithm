#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    for x in range(n):
        if computers[x][x] == 1:
            answer += 1
            dfs(x, n, computers)
                      
    return answer

def dfs(x, n, computers):
    if computers[x][x] == 1:
        computers[x][x] = 0
        for a in range(n):
            if computers[x][a] == 1:
                dfs(a, n, computers)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	), 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	), 1)
print(solution(3, [[1, 1, 1], [1, 1, 1], [0, 0, 1]]	), 1)
print(solution(3, [[1,1,1],[1,1,1],[1,1,1]]	), 1)
print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]), 2)
print(solution(7, [
    [1,0,0,0,0,0,1],
    [0,1,1,0,1,0,0],
    [0,1,1,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,1,0,0,1,1,0],
    [0,0,0,0,1,1,1],
    [1,0,0,0,0,1,1]
]), 1)
