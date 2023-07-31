# n, m = map(int, input().split())

n, m = 4, 2

answer = []
check = [False for _ in range(n+1)]

def dfs(i, sum):
    global check, m, answer

    if sum == m: 
        print(*answer)
        return

    for j in range(i + 1, n+1):
        answer.append(j)
        dfs(j, sum + 1)
        answer.pop()

dfs(0, 0)
