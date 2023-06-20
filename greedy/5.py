#https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq

def solution(n, costs):
    bridges = [[False if col != row else 0 for col in range(n)] for row in range(n)]
    for bridge in costs:
        bridges[bridge[0]][bridge[1]] = bridges[bridge[1]][bridge[0]] = bridge[2]

    minHeap = [(0, 0, 0)]
    visited = []
    answer = 0

    while minHeap:
        temp = heapq.heappop(minHeap)
        if temp[1] in visited and temp[2] in visited: continue
        answer = answer + temp[0]
        for index in range(2):
            if temp[index+1] not in visited:
                for idx, cost in enumerate(bridges[temp[index+1]]):
                    if cost != False and temp[index+1] != idx:
                        heapq.heappush(minHeap, (cost, temp[index+1], idx))
                visited.append(temp[index+1])
            
    return answer


result = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(result, result == 4)

result = solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])
print(result, result == 159)

result = solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])
print(result, result == 15)

result = solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])
print(result, result == 8)

result = solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])
print(result, result == 9)

result = solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])
print(result, result == 104)

result = solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
print(result, result == 11)

result = solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]])
print(result, result == 6)

result = solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]])
print(result, result == 8)

result = solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])
print(result, result == 8)

result = solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]])
print(result, result == 7)

result = solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])
print(result, result == 8)

result = solution(4, [[0,1,1],[0,2,2],[2,3,1]])
print(result, result == 4)
