#https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    graph = [[] for _ in range(n+1)]
    for a, b in results:
        graph[b].append(a)
            
    
    q, rank, first = [0], [set() for _ in range(n+1)], set()
    def find(n):
        if len(graph[n]) < 1: 
            first.add(n)
            return {n}
        
        if len(rank[n]) < 1:
            for winner in graph[n]:
                rank[n].update(find(winner))
        return rank[n]
        
    for i in range(1, n+1):
        find(i)
        
    return sum(map(lambda x: 1 if x == first else 0, rank))


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)