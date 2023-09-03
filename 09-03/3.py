from itertools import combinations

def solution(arr, k, t):
    answer = 0
    
    for length in range(k, len(arr)+1):
        for cases in combinations(arr, length):
            if sum(cases) <= t: answer += 1

    return answer

print(solution([2,5,3,8,1],3,11),6)
print(solution([1,1,2,2],2,3),5)
print(solution([1,2,3,2],2,2),0)
