
def solution(v):
    rows, cols = len(v), len(v[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    cnt, maxArea = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for row in range(rows):
        for col in range(cols):
            if v[row][col] == 1 and not visited[row][col]:
                cnt += 1
                visited[row][col] = True
                queue, area = [(row, col)], 1

                while queue:
                    curRow, curCol = queue.pop(0)
                    for dr, dc in directions:
                        newRow, newCol = curRow + dr, curCol + dc
                        if 0 <= newRow < rows and 0 <= newCol < cols:
                            if v[newRow][newCol] == 1 and not visited[newRow][newCol]:
                                queue.append((newRow, newCol))
                                visited[newRow][newCol] = True
                                area += 1

                maxArea = max(maxArea, area)

    return [cnt, maxArea]


print(solution([[1,1,0,1,1], [0,1,1,0,0], [0,0,0,0,0], [1,1,0,1,1], [1,0,1,1,1], [1,0,1,1,1]]), [4,8])