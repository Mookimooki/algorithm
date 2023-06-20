#https://cote.inflearn.com/contest/10/problem/09-04

import heapq

# n = int(input())
# schedule = []

# for m in range(n):
#     input1, input2 = map(int, input().split())
#     schedule.append([input1, input2])
    
n = 6
schedule = [[50, 2], [20, 1], [40, 2], [60, 3], [30, 3], [30, 1]]
schedule.sort(key = lambda friend: (-friend[1], -friend[0]))

q = []

idx=0
answer=0
for num in range(max(schedule, key=lambda x: x[1])[1], 0, -1):
    while(idx < len(schedule) and schedule[idx][1] == num):
        heapq.heappush(q, -schedule[idx][0])
        idx += 1
    if len(q) > 0:
        answer -= heapq.heappop(q)
print(answer)