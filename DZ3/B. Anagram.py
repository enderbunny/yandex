a = list(map(str, input()))
b = list(map(str, input()))

if sorted(a) == sorted(b):
    print('YES')
else:
    print('NO')
