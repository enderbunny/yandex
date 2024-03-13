n, k = map(int, input().split())
days = list(map(int, input().split())) + [0] * k
profit = [0]
prof = 0

while n != 0:
    if days[n-1+k] - days[n-1] > prof:
        prof = days[n-1+k] - days[n-1]
    profit.append(days[n-1+k] - days[n-1])
    n -= 1

print(days)
print(profit)
print(prof)
