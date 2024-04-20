n, k = map(int, input().split())
days = list(map(int, input().split())) + [0] * k
arr = [0] * n
total = 0
best_prof = [0, days[0]]

for i in range(n):
    if best_prof[1] >= days[i] or arr[best_prof[0]] + 1 > k:
        best_prof = [i, days[i]]
    arr[best_prof[0]] += 1
    total += best_prof[1]


print(total)
print(' '.join(map(str, arr)))
