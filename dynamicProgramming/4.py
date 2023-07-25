#https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
def solution(m, n, puddles):
    grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
    grid[0][1] = 1
    
    for puddle in puddles:
        grid[puddle[1]][puddle[0]] = -1
    
    for rowIdx in range(1, n+1):
        for colIdx in range(1, m+1):
            if grid[rowIdx][colIdx] == -1:
                grid[rowIdx][colIdx] = 0
                continue
            grid[rowIdx][colIdx] = grid[rowIdx -1][colIdx] + grid[rowIdx][colIdx -1]
    
    return grid[-1][-1] % 1000000007

print(solution(4, 3, [[2, 2],[3, 1]]))