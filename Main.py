n = int(input())
good = {}
bed = {}
max_hi = 0
position = []
res = []


for i in range(1, n + 1):
    up, down = map(int, input().split())
    if up - down > 0:
        good[i] = [up, down, up - down]
    else:
        bed[i] = [up, down, up - down]
    # berries[i] = [up, down, up - down]

good = sorted(good.items(), key=lambda item: item[1][2], reverse=True)
bed = sorted(bed.items(), key=lambda item: item[1][0], reverse=True)
berries = good + bed
# berries1 = dict(berries1)
print(berries)
pos = 0
for el in berries:
    res.append(el[0])
    print(pos, end=' - ')
    print(pos + el[1][0], end=' - ')
    position.append(pos + el[1][0])
    pos = pos + el[1][2]
    print(pos)

print(max(position))
print(" ".join(map(str, res)))
