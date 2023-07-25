#https://school.programmers.co.kr/learn/courses/30/lessons/1843
#https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.4-%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0
from sys import maxsize

def solution(arr):
    length = (len(arr) + 1) // 2
    MAX_DP = [[-maxsize for _ in range(length)] for _ in range(length)]
    MIN_DP = [[maxsize for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        MAX_DP[i][i] = MIN_DP[i][i] = int(arr[i*2])
    
    for step in range(1, length):
        for start in range(length - step):
            end = start + step        
            for j in range(start+1, start+step+1):
                if arr[j*2-1] == '+':
                    MAX_DP[start][end] = max(MAX_DP[start][end], MAX_DP[start][j-1] + MAX_DP[j][end])
                    MIN_DP[start][end] = min(MIN_DP[start][end], MIN_DP[start][j-1] + MAX_DP[j][end])
                else:
                    MAX_DP[start][end] = max(MAX_DP[start][end], MIN_DP[start][j-1] - MIN_DP[j][end])
                    MIN_DP[start][end] = min(MIN_DP[start][end], MIN_DP[start][j-1] - MAX_DP[j][end])
        
    return MAX_DP[0][length-1]

print(solution(["1", "-", "3", "+", "5", "-", "8"])) #1
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])) #3