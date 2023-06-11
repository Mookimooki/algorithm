#https://cote.inflearn.com/contest/10/problem/10-06

n, m = map(int, input().split())
problems = []
for i in range(n):
    score, time = map(int, input().split())
    problems.append((score, time))

# n = 5
# m = 20
# problems = [[10,  5],[25, 12],[15, 8],[6, 3],[7, 4]]
problems.sort(key=lambda x: x[1])

dy=[0 if x==0 else -1 for x in range(m+1)]
def rec(minutes):
    if minutes < problems[0][1]: 
        return 0
    if dy[minutes] < 0:
        for prob in problems: # prob = (점수, 시간)
            if minutes-prob[1] >= 0:
                dy[minutes] = max(dy[minutes], rec(minutes-prob[1]) + prob[0])
    return dy[minutes]
    
result = rec(m)
print(result)