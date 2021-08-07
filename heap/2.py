import heapq

def solution(jobs):
    sec = 0
    heap = []
    candidate = []
    avg = 0

    for at, length in jobs:
        heapq.heappush(heap, (at, length))

    while heap or candidate:
        while (heap and heap[0][0] <= sec) or not candidate :
            el = heapq.heappop(heap)
            heapq.heappush(candidate, (el[1], el[0], el[1]))

        el = heapq.heappop(candidate)
        sec = max(el[1], sec)
        sec += el[2]
        avg += sec - el[1]

    return avg / len(jobs)

print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))