#https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1
        
    def bfs(row, col, val):
        for idx in range(1, n+1):
            el = graph[col][idx]
            if el != val: continue
            graph[row][idx] = val
            graph[idx][row] = -val
        
    for row in range(1, n+1):
        for col in range(1, n+1):
            if graph[row][col] == 0: continue
            bfs(row, col, graph[row][col])
    
    answer = 0
    for row in range(1, n+1):
        if sum(map(abs, graph[row])) == n-1: answer += 1 
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
