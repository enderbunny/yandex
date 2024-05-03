n = int(input())
x, y = [], []

while n != 0:
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
    n -= 1

print(min(x), min(y), max(x), max(y))