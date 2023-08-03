import sys
input = sys.stdin.readline

m, n = map(int, input().split())

tomatoes = []
q = []
answer = 0
for x in range(n):
    temp = list(map(int, input().split()))
    for y in range(m):
        if temp[y] == 1:
            q.append((x, y))
            answer = 1
    tomatoes.append(temp)

while len(q) > 0:
    x, y = q.pop(0)
    temp = [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]
    
    for a, b in temp:
        if a < 0 or a == n or b < 0 or b == m:
            continue
        
        if tomatoes[a][b] == 0:
            answer = tomatoes[a][b] = tomatoes[x][y]+1
            q.append((a, b))
    
print(answer-1)
    