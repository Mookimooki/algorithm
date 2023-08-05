import heapq

def solution1(distance, rocks, n):
    rocks.sort()
    heap = []
    length = len(rocks)
    heapq.heappush(heap, (rocks[0], 0))
    heapq.heappush(heap, (distance - rocks[-1], length))
    for i in range(1, len(rocks)):
        heapq.heappush(heap, (rocks[i]-rocks[i-1], i))
    
    distanceByRocks = [rocks[0]] + [rocks[i+1]-rocks[i] for i in range(length-1)] + [distance - rocks[-1]] # i번째는 rocks[i]
    
    answer, idx = heapq.heappop(heap)
    for _ in range(n):
        distanceByRocks[idx] = -1
        j = 1
        while distanceByRocks[idx+j] < 0:
            j+=1
        distanceByRocks[idx+j] += answer 
        while distanceByRocks[idx] != answer:
            if distanceByRocks[idx] > 0:
                heapq.heappush(heap, (distanceByRocks[idx], idx))
            answer, idx = heapq.heappop(heap)
    return answer

def solution(distance, rocks, n):
    rocks = sorted(rocks) + [distance]
    
    answer = 0
    left, right = 1, distance
    while (left <= right):
        mid = int((left + right) / 2)
        cnt = 0
        prev = 0
        for i in range(len(rocks)):
            if (rocks[i] - prev < mid):
                cnt += 1
            else:
                prev = rocks[i]
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer

# 정확성: 20.5
# 합계: 20.5 / 100.0

print(solution(25, [2, 14, 11, 21, 17], 2), 4)
print(solution(23, [3, 6, 9, 10, 14, 17], 2), 3)
print(solution(16, [4, 8, 11], 2), 8)
print(solution(16, [4, 8], 1), 8)
print(solution(23, [3, 6, 9, 10, 14, 17], 2), 3)
# print(solution(1000000000, [x+10 for x in range(50000, 0, -1)], 50000), 'tttt')