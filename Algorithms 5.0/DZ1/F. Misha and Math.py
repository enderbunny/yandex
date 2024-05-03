n = int(input())
data = list(map(int, input().split(' ')))
res = ''
a = data[0] % 2 == 0

while len(res) != n - 1:
    if a or data[len(res) + 1] % 2 == 0:
        a = a and data[len(res) + 1] % 2 == 0
        res += '+'
    else:
        res += 'x'

print(res)