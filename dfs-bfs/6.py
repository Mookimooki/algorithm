def solution(rectangles, characterX, characterY, itemX, itemY):
    queue, visited = [(characterX, characterY, 0)], [[False for _ in range(60)] for _ in range(60)]
    ways = [[(0.5, 0),(-0.5, 0),(0, 0.5),(0, -0.5)], [(1, 0),(-1, 0),(0, 1),(0, -1)]]
    
    while len(queue) > 0:
        posX, posY, val = queue.pop(0)
        if posX == itemX and posY == itemY: return val
        if visited[posX][posY]: continue
        visited[posX][posY] = True
        
        for i in range(len(ways[0])):
            dirX, diY, x, y = posX + ways[0][i][0], posY + ways[0][i][1], posX + ways[1][i][0], posY + ways[1][i][1]
            if visited[x][y] or isInside(rectangles, dirX, diY): continue
            
            if isOnRectengle(rectangles, dirX, diY):
                queue.append((x, y, val+1))

def isInside(rectangles, posX, posY):
    for x1, y1, x2, y2 in rectangles:
        if x1 < posX and posX < x2 and y1 < posY and posY < y2: 
            return True
    return False

def isOnRectengle(rectangles, posX, posY):
    for x1, y1, x2, y2 in rectangles:
        if y1 == posY or y2 == posY:
            if x1 <= posX and posX <= x2:            
                return True
        elif x1 == posX or posX == x2:
            if y1 < posY and posY < y2:
                return True
    return False

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8), 17)
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7,	6, 1), 11)
print(solution([[1,1,5,7]],	1,	1,	4,	7,	), 9)
print(solution([[2,1,7,5],[6,4,10,10]],	3,	1,	7,	10	), 15)
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],	1,	4,	6,	3	), 10)