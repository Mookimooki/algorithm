#https://cote.inflearn.com/contest/10/problem/10-04

# n = int(input())
# rocks = []

# for i in range(n):
#     s, h, w = map(int, input().split())
#     rocks.append((s, h, w))

n = 5
rocks = [[25, 3, 4],[4, 4, 6],[9, 2, 3],[16, 2, 5],[1, 5, 2]]
    
rocks.sort(key=lambda x: -x[0])
dy = []

for i in range(n):
    maxHeight = 0
    for j in range(i):
        if rocks[j][2] > rocks[i][2]: 
            maxHeight = max(maxHeight, dy[j])
    dy.append(maxHeight + rocks[i][1])

print(max(dy))