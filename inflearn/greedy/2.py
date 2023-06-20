#https://cote.inflearn.com/contest/10/problem/09-02

n = int(input())
meetings = []

for m in range(n):
    input1, input2 = map(int, input().split())
    meetings.append([input1, input2])
    
# meetings = [[3, 3], [1, 3], [2, 3]]
meetings.sort(key = lambda meeting: (meeting[1], meeting[0]))

answer = 0
lastEnd = 0
for meeting in meetings:
    if meeting[0] >= lastEnd:
        answer += 1
        lastEnd = max(lastEnd, meeting[1])

print(answer)