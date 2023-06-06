#https://cote.inflearn.com/contest/10/problem/09-07

# v, numOfPairs = map(int, input().split())
edges = []

# for m in range(numOfPairs+1):
#     input1, input2 = map(int, input().split())
#     edges.append([input1, input2])

v = 9
numOfPairs = 12
edges = [
    [1, 2, 12],
    [1, 9, 25],
    [2, 3, 10],
    [2, 8, 17],
    [2, 9, 8],
    [3, 4, 18],
    [3, 7, 55],
    [4, 5, 44],
    [5, 6, 60],
    [5, 7, 38],
    [7, 8, 35],
    [8, 9, 15]
]

unf = [x for x in range(v+1)]

edges.sort(key=lambda x: x[2])

def find(a):
    if unf[a] == a: return a
    unf[a] = find(unf[a])
    return unf[a]

def union(a, b):
    v1 = find(a)
    v2 = find(b)
    unf[v1] = v2

sum = 0
for edge in edges:
    v1 = find(edge[0])
    v2 = find(edge[1])
    if v1 == v2: continue
    
    union(v1, v2)
    sum = sum + edge[2]
    
print(sum)