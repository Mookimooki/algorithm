#https://cote.inflearn.com/contest/10/problem/10-06

n, m = map(int, input().split())
problems = []
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time))

# n = 5
# m = 20
# problems = [[10,  5],[25, 12],[15, 8],[6, 3],[7, 4]] # [점수, 시간]

dy=[0 for x in range(m+1)]
result = []

for problem in problems:
    for i in range(m ,problem[1]-1, -1):
        dy[i] = max(dy[i], dy[i-problem[1]] + problem[0])


print(dy[m])