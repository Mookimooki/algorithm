def solution(happiness):
    dp = [True if x > 8 else False for x in happiness]
    
    maxCnt = 0
    happyCnt = 0
    wholeCnt = 0
    
    for idx in range(len(dp)):
        happyDay = dp[idx]
        if happyDay:
            happyCnt += 1
        wholeCnt += 1
        
        if happyCnt > wholeCnt / 2:
            maxCnt = max(maxCnt, wholeCnt)
        else:
            temp = idx -1
            while(wholeCnt > 1):
                wholeCnt -= 1
                dp[temp] = 0
                temp -= 1
            wholeCnt = 0
            happyCnt = 0
        
    return maxCnt

# print(solution([9, 10, 6, 0, 4, 6, 10]))
print(solution([6, 10, 3, 9, 4, 10, 3, 9, 3, 10, 6]))
