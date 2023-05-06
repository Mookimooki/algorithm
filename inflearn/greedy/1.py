#https://cote.inflearn.com/contest/10/problem/09-01

# n = int(input())
# bodies = []

# for m in range(n):
#     input1, input2 = map(int, input().split())
#     bodies.append([input1, input2])
    
bodies = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]] 
bodies.sort(key = lambda body: [-body[0]])

answer = 0
maxWeight = 0
for body in bodies:
    if body[1] >= maxWeight:
        answer += 1
    maxWeight = max(maxWeight, body[1])

print(answer)