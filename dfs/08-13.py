n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
stack = []
answer = 0

for a in range(n):
    for b in range(n):
        if map[a][b] == 1 and not visited[a][b]:
            answer += 1
            stack.append((a, b))
            while len(stack) > 0:
                x, y = stack.pop()
                if x < 0 or x == n or y < 0 or y == n or map[x][y] == 0 or visited[x][y]: continue
                visited[x][y] = True
                stack.extend([(x+1, y),(x-1, y),(x, y+1),(x, y-1),(x+1, y+1),(x-1, y+1),(x+1, y-1),(x-1, y-1)])

print(answer)