#https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq
import sys

def solution(n, costs):
    bridges = [[False if col != row else 0 for col in range(n)] for row in range(n)]
    for bridge in costs:
        bridges[bridge[0]][bridge[1]] = bridges[bridge[1]][bridge[0]] = bridge[2]

    dist = [sys.maxsize for i in range(n)]
    visited = [False for i in range(n)]

    minHeap = [(0, 0)]
    dist[0] = 0

    while minHeap:
        temp = heapq.heappop(minHeap)
        cost = temp[0]
        node = temp[1]

        if visited[node]: continue
        visited[node] = True

        dest = 0
        while dest < n:
            if visited[dest] != True and bridges[node][dest] != False:
                heapq.heappush(minHeap, (bridges[node][dest], dest))
                newCost = cost + bridges[node][dest]
                if dist[dest] > newCost:
                    dist[dest] = newCost
                else:
                    # print(node, dest, bridges[node][dest])
                    bridges[node][dest] = bridges[dest][node] = False
            dest += 1

    answer = 0
    for row in bridges:
        answer += sum(row)
    return answer // 2


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








