from itertools import combinations
from sys import maxsize

n, m = map(int, input().split())
houses = []
pizzaShop = []

for x in range(n):
    for y, val in enumerate(map(int, input().split())):
        if val == 1:
            houses.append((x, y))
        elif val == 2:
            pizzaShop.append((x, y))

answer = maxsize
for comb in combinations(pizzaShop, m):
    distanceOfCity = 0
    for house in houses:
        distance = maxsize
        for shop in comb:
            distance = min(distance, abs(house[0] - shop[0])+abs(house[1] - shop[1]))
        distanceOfCity += distance
    answer = min(answer, distanceOfCity)
print(answer)
