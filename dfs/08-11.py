maze = []
size = 7
# for _ in range(size):
#     maze.append(list(map(int, input().split())))
maze = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0]]


def bfs(x, y):
    check = [[False for _ in range(size)] for _ in range(size)]
    stack = []
    next= [(x, y)]
    answer = 0

    while len(next) > 0:
        stack = next
        next = []
        while len(stack) > 0:
            x, y = stack.pop()
            if x < 0 or x == size or y == size or y < 0 or maze[x][y] == 1 or check[x][y]:
                continue
            check[x][y] = True
            if x == size - 1 and y == size - 1:
                return answer
            else:
                next.extend([(x+1, y),(x-1, y),(x, y-1),(x, y+1)])
        answer += 1
    return -1
print(bfs(0, 0))