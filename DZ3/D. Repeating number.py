n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 'NO'
i = 0
while res == 'NO' and i + k < n:
    if a[i] in a[i+1:i+k+1]:
        res = 'YES'
    i += 1

print(res)
