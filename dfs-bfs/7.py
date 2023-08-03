#https://school.programmers.co.kr/learn/courses/30/lessons/84021

def solution(game_board, table):
    size = len(game_board)
    spaces, puzzles = [], []
    
    for num, board, peices in zip((0, 1),(game_board, table),(spaces, puzzles)):
        visited = [[False for _ in range(size)]for _ in range(size)]
        
        for x in range(size):
            for y in range(size):
                if visited[x][y] or board[x][y] != num: continue
                peice, q = [], [(x, y)]
                
                while len(q) > 0:
                    a, b = q.pop(0)
                    if a < 0 or a == size or b < 0 or b == size or visited[a][b] or board[a][b] != num: continue
                    visited[a][b] = True
                    peice.append((a, b))
                    q.extend([(a+1, b),(a-1, b),(a, b+1),(a, b-1)])
                if len(peice) > 0: peices.append(normalizePeice(peice))
    
    answer = 0
    for puzzle in puzzles:
        for _ in range(4):
            if puzzle in spaces:
                answer += sum(map(sum, puzzle))
                spaces.remove(puzzle)
                break
            puzzle = [[row[i] for row in puzzle[::-1]] for i in range(len(puzzle[0]))]
            
    return answer
    
def normalizePeice(peice):
    x1, y1, x2, y2 = 50, 50, 0, 0
    for coord in peice:
        x1, y1 = min(x1, coord[0]), min(y1, coord[1])
        x2, y2 = max(x2, coord[0]), max(y2, coord[1])
    matrix = [[0 for _ in range(y2-y1+1)] for _ in range(x2-x1+1)]
    for x, y in peice:
        matrix[x-x1][y-y1] = 1
    return matrix
    

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]),	14)
print(solution([[0,0,0],[1,1,0],[1,1,1]],	[[1,1,1],[1,0,0],[0,0,0]]),	0)
      
