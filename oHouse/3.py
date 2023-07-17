def solution(grid):
    n = len(grid) # row
    m = len(grid[0]) # col
    
    visited = [[False for _ in range(m) ] for _ in range(n)]
    maxSize = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == False:
                size = 1
                q = [(i, j)]
                visited[i][j] = True

                while len(q) > 0:
                    coord = q.pop(0)
                    
                    dx = [-1 ,0, 1, 0]
                    dy = [0, -1, 0, 1]
                    
                    for k in range(4):
                        nx = coord[0] + dx[k]
                        ny = coord[1] + dy[k]

                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if visited[nx][ny]:
                            continue
                        if grid[nx][ny] == 1:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            size = size + 1
                
                maxSize = max(maxSize, size)
    
    return maxSize

# print(solution([[1,1,0], [1,1,0], [0,0,1], [0,0,1]]))
# print(solution([[0,1,0]]))
print(solution([[0],[1],[0]]))
print(solution([[0],[0],[0]]))