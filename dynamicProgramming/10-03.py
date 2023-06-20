#https://cote.inflearn.com/contest/10/problem/10-03

# n = int(input())
# arr = list(map(int, input().split()))

n=8
arr = [5, 3, 7, 8, 6, 2, 9, 4]
dp = []

for i in range(n):
    num = arr[i]
    length = 1
    for j in range(i, 0, -1):
        if arr[j] < num:
            length = max(length, dp[j] + 1)
    dp.append(length)

print(max(dp))