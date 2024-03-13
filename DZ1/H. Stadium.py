arr = list(map(int, input().split(' ')))

L = arr[0]
x1 = arr[1]
v1 = arr[2]
x2 = arr[3]
v2 = arr[4]

x = (v1 - v2) / (x1 * v2 - x2 * v1)

print(x / v1)