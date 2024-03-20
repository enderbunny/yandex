n = int(input())
a = list(map(int, input().split()))

ed_a = list(set(a))
count = n
print(ed_a)

for i in range(len(ed_a)):
    if ed_a[i] - ed_a[i + 1] == -1 and count > (n - (a.count(ed_a[i]) + a.count(ed_a[i + 1]))):
        print(ed_a[i], ed_a[i + 1])
        count = n - (a.count(ed_a[i]) + a.count(ed_a[i + 1]))

print(count)

