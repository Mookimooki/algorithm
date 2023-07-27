n = int(input())
arr = list(map(int, input().split()))
answer = sum(arr)
flag = False
result = 'NO'

def dfs(i, sum):
    global flag
    if flag or sum > answer or i == n: return
    if sum == answer: 
        flag = True
        global result
        result = 'YES'
        return
    
    dfs(i+1, sum+arr[i])
    dfs(i+1, sum)

if answer % 2 == 0: 
    answer //= 2
    dfs(0, 0)

print(result)

        
        