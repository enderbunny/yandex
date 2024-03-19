n = int(input())
a = list(map(int, input().split()))

new_a = []
otr = []

for i in range(n):
    if len(otr) + 1 == a[i] or len(otr) + 1 == min(otr, default=0):
        print(1, i, otr, end='-')
        otr.append(a[i])
        new_a.append(otr)
        print(otr)
        otr = []
    elif len(otr) + 1 < a[i]:
        print(2, i, otr, end='-')
        otr.append(a[i])
        print(otr)

    else:
        new_a.append(otr)
        print(3, i, new_a)
        otr = [a[i]]

# new_a.append(otr)

print(len(new_a))
print(new_a)
