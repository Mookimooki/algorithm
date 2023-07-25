def solution(happiness):
    happiness = [1 if x > 8 else -1 for x in happiness]
    length = len(happiness)
    
    dp = [[0 for _ in range(length)] for _ in range(length)]
    
    maxDays = 0
    for i in range(length):
        for j in range(i, length):
            if i == j: dp[i][i] = happiness[i] 
            else: dp[i][j] = dp[i][j-1] + happiness[j]
            
            if dp[i][j] >= 1:
                maxDays = max(maxDays, j - i + 1)

    return maxDays

print(solution([9, 10, 6, 0, 4, 6, 10]), 3) 
print(solution([6, 10, 3, 9, 4, 10, 3, 9, 3, 10, 6]), 9)
print(solution([5, 3, 1, 3, 6, 4]), 0)
