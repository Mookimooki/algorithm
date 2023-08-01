maze = []
size = 7
for _ in range(size):
    maze.append(list(map(int, input().split())))
# maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
check = [[False for _ in range(size)] for _ in range(size)]
answer = 0

def dfs(x, y):
    global answer, size

    if x < 0 or x == size or y == size or y < 0 or maze[x][y] == 1 or check[x][y]:
        return
    
    check[x][y] = True
    if x == size - 1 and y == size - 1:
        answer += 1
    else:
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
    check[x][y] = False

dfs(0, 0)

print(answer)