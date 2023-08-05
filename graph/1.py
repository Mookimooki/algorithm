#https://school.programmers.co.kr/learn/courses/30/parts/14393

def solution(n, edge):
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for s, e in edge:
        graph[s][e] = graph[e][s] = 1
        
    visited = [False for _ in range(n+1)]
    q = [1]
    maxVal, maxCnt = 0, 0
    
    while len(q) > 0:
        node = q.pop(0)        
        for i in range(2, n+1):
            if not visited[i] and graph[node][i] == 1:
                visited[i] = True
                val = graph[1][i] = graph[1][node] + 1
                q.append(i)
                
                if maxVal < val: 
                    maxCnt = 1
                    maxVal = max(maxVal, val)
                elif maxVal == val: maxCnt += 1
                
    return maxCnt


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))