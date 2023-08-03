#https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    tickets.sort(key=lambda x: (x[0] != 'ICN', x[1]))
    return dfs('ICN', ['ICN'], tickets, [False for _ in range(len(tickets))])

def dfs(s, stack, tickets, visited):
    if len(tickets) < len(stack):
        return stack
    
    for i in range(len(tickets)):
        if not visited[i] and s == tickets[i][0]:
            visited[i] = True
            result = dfs(tickets[i][1], stack + [tickets[i][1]], tickets, visited)
            if result != None: return result
            visited[i] = False
    
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ICN", "SFO"], ["ATL","SFO"]])) 