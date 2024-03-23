from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))

count = 0

for el in a:
    if count < a[el] + a[el+1]:
        count = a[el] + a[el+1]

print(n - count)

# arr = [a.count(el) + a.count(el+1) for el in a]
