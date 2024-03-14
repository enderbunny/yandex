n, k = map(int, input().split())
days = list(map(int, input().split())) + [0] * k
profit = 0

while n != 0:
    for i in range(1, k+1):
        if days[n-1+i] - days[n-1] > profit:
            profit = days[n-1+i] - days[n-1]
    n -= 1

print(profit)