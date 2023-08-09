#https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    graph, first = [[] for _ in range(n+1)], [x+1 for x in range(n)]
    for a, b in results:
        graph[a].append(b)
        if b in first: first.remove(b)
        
    for i in first:
        if len(graph[i]) == 0: graph[0].append(i)
        
    q, rank = [0], [0 for _ in range(n+1)]
    while len(q) > 0:
        winner = q.pop(0)
        for loser in graph[winner]:
            rank[loser] = rank[winner] + 1
            q.append(loser)
        
    answer = 0
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
