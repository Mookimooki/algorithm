import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for x in scoville:
        heapq.heappush(heap, x)
    
    while len(heap) > 1 and heap[0] < K:
        heapq.heappush(heap, (heapq.heappop(heap) + heapq.heappop(heap) * 2))
        answer += 1
    
    if heap[0] < K:
        return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))