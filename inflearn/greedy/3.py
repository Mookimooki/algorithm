#https://cote.inflearn.com/contest/10/problem/09-03

n = int(input())
friends = []

for m in range(n):
    input1, input2 = map(int, input().split())
    friends.append([input1, input2])
    
# friends = [[14, 18], [12, 15], [15, 20], [20, 30], [5, 14]]

schedule = []
for friend in friends:
    schedule.append((friend[0], 'S'))
    schedule.append((friend[1], 'E'))
schedule.sort(key = lambda friend: (friend[0], friend[1]))

count = 0
maxCount = 0
for friend in schedule:
    if friend[1] == 'S':
        count += 1
    else:
        count -= 1
    maxCount = max(maxCount, count)

print(maxCount)