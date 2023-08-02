#https://cote.inflearn.com/contest/10/problem/08-07

n, r = map(int, input().split())
dp = [[0 for _ in range(r+1)] for _ in range(n+1)]

def dfs(n, r):
    if r == 0 or n == r: 
        dp[n][r] = 1
        return 1
    if dp[n][r] < 1:
        dp[n][r] = dfs(n-1, r-1) + dfs(n-1, r)
    return dp[n][r]
    
print(dfs(n, r))