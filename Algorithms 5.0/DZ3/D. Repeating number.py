n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 'NO'
i = 0
set_k = set()
while res == 'NO' and i < n:
    if a[i] in set_k:
        res = 'YES'
    set_k.add(a[i])
    if i >= k:
        set_k.remove(a[i-k])
    i += 1

print(res)
