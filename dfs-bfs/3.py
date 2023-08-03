#https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = [(0, 0)]
    
    while len(queue) > 0:
        x, y = queue.pop(0)
        if x == n-1 and y == m-1: 
            return maps[x][y]
        
        for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if a < 0 or a == n or b < 0 or b == m or maps[a][b] != 1: continue
            maps[a][b] = maps[x][y] + 1
            queue.append((a, b))
        
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
