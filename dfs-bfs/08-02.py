c, n = map(int, input().split())
dogs = []
maxWeight = 0

for _ in range(n):
    dogs.append(int(input()))

def dfs(i, sum, dogs):
    global maxWeight, c
    if c < sum : return
    if i == n:
        maxWeight = max(maxWeight, sum)
        return
    
    dfs(i+1, sum, dogs)
    dfs(i+1, sum + dogs[i], dogs)
dfs(0, 0, dogs)
print(maxWeight)