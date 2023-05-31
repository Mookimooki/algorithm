#https://cote.inflearn.com/contest/10/problem/09-06

# n, numOfPairs = map(int, input().split())
# friends = []

# for m in range(n):
#     input1, input2 = map(int, input().split())
#     friends.append([input1, input2])


n = 9
numOfPairs = 7
friends = [
    [1, 2],[2, 3],[3, 4],[1, 5],[6, 7],[7, 8],[8, 9],[3, 8]
]
unf = [x for x in range(n+1)]

def find(a):
    if unf[a] == a: return a
    unf[a] = find(unf[a])
    return unf[a]

def union(a, b):
    f1 = find(a)
    f2 = find(b)
    unf[f1] = f2

for idx in range(numOfPairs):
    union(friends[idx][0], friends[idx][1])

f1 = find(friends[numOfPairs][0])
f2 = find(friends[numOfPairs][1])

if f1 == f2:
    print('YES')
else:
    print('NO')