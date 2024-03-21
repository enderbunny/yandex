n = int(input())
a = list(map(int, input().split()))

un_a1 = list(set(a))
count = 0

for el in un_a1:
    if count < a.count(el) + a.count(el+1):
        count = a.count(el) + a.count(el+1)

print(n - count)
