import math

n, f = map(int, input().split())
# n, f = 5, 39

product = [math.comb(n-1, x) for x in range(n)]
chk = [False for x in range(n + 1)]
answer = []
flag = False

def dfs(i, sum):
    global product, chk, f, answer, flag
    if sum > f: return
    if sum == f:
        if len(answer) == n:
            flag = True
            print(*answer)
        return
    
    for j in range(1, n + 1):
        if chk[j] == False:
            chk[j] = True
            answer.append(j)
            dfs(i+1, sum + j * product[i])
            if flag: break
            answer.pop()
            chk[j] = False

dfs(0, 0)
