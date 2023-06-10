#https://cote.inflearn.com/contest/10/problem/10-05

# n = 3
# coins = [1,2,5]
# sum=15

n = int(input())
coins = list(map(int, input().split()))
sum = int(input())

dy=[x for x in range(sum+1)]

for coin in coins:
    if coin != 1:
        for j in range(coin, sum+1):
            dy[j] = min(dy[j], dy[j-coin] + 1)            
            
print(dy[sum])