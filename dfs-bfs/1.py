#https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):    
    return dfs(0, 0, numbers, target)

def dfs(index, sum, numbers, target):
    if index == len(numbers):
        if sum == target: return 1
        else: return 0
    
    return dfs(index + 1, sum + numbers[index], numbers, target) + dfs(index + 1, sum - numbers[index], numbers, target)

print(solution([1, 1, 1, 1, 1], 3), 5)
print(solution([4, 1, 2, 1]	, 4), 2)