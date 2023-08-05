#https://school.programmers.co.kr/learn/courses/30/parts/14393

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
        
    visited, disatance = [False for _ in range(n+1)], [0 for _ in range(n+1)]
    maxVal, maxCnt = 0, 0
    
    q = [1]
    visited[1] = True
    
    while len(q) > 0:
        node = q.pop(0)        
        for dest in graph[node]:
            if not visited[dest]:
                visited[dest] = True
                val = disatance[dest] = disatance[node] + 1
                q.append(dest)
                
                if maxVal < val: 
                    maxCnt = 1
                    maxVal = max(maxVal, val)
                elif maxVal == val: maxCnt += 1
                
    return maxCnt


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))