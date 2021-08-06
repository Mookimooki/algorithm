import heapq

def solution(prices):
    queue = []
    answer = []

    for idx, el in enumerate(prices):
        while len(queue) > 0 and queue[0][0] < -el:
            temp = heapq.heappop(queue)
            answer.append((temp[1], idx-temp[1]))
        heapq.heappush(queue, (-el, idx))
    else:
        answer.extend([(idx, len(prices)-idx-1) for el, idx in queue])
    return [el for idx, el in sorted(answer, key = lambda x: x[0])]

print(solution([1, 2, 3, 2, 3, 1]))