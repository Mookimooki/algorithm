from itertools import combinations

def findMinDistance(way):
    answer = way[-1]
    for i in range(1, len(way)):
        answer = min(answer , way[i] - way[i-1])
    return answer

def solution(distance, rocks, n):
    rocks.sort()
    lt, rt = 1, distance - rocks[-1]
    
    ways = tuple(map(lambda x: (0,) + x + (distance,), combinations(rocks, len(rocks) - n)))
    # answer = 0
    # while lt <= rt:
    #     mid = (lt + rt)//2
    #     if max(map(findMinDistance, ways)) >= mid:
    #         answer = mid
    #         rt = mid - 1
    #     else:
    #         lt = mid + 1
    # return answer
    return max(map(findMinDistance, ways))
#정확성: 12.8
#합계: 12.8 / 100.0

print(solution(25, [2, 14, 11, 21, 17], 2))