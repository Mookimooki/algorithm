#https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    length = len(money)
    dp = [0 for _ in range(length)]
    dp[0], dp[1] = money[0], money[1]
    
    for i in range(2, length-1):
        dp[i] = max(dp[i-3], dp[i-2]) + money[i]
    
    answer = max(dp[-3:])
    dp[0], dp[2] = 0, money[2]
    for i in range(3, length):
        dp[i] = max(dp[i-3], dp[i-2]) + money[i]
    
    return max(answer, max(dp[-2:]))

def solution1(money):
    x1, y1, z1 = money[0], money[1], money[0] + money[2]
    x2, y2, z2 = 0, money[1], money[2]
    for i in money[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + i
        x2, y2, z2 = y2, z2, max(x2, y2) + i
    return max(x1, y1, y2, z2)

print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)