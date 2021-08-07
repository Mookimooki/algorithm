import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    len = 0

    for x in operations:
        num = int(x.split()[1])

        if x.startswith('I'):
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, -num)
            len += 1
        elif len > 0:
            len -= 1
            if num < 0:
                heapq.heappop(minHeap)
            elif num > 0:
                heapq.heappop(maxHeap)
        if len == 0:
            minHeap = []
            maxHeap = []

    if len == 0:
        return [0, 0]
    
    return [-maxHeap[0], minHeap[0]]
        

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))