n = int(input())
good = {}
bed = {}
position = []
res = []


for i in range(1, n + 1):
    up, down = map(int, input().split())
    if up - down > 0:
        good[i] = [up, down, up - down]
    else:
        bed[i] = [up, down, up - down]

good = sorted(good.items(), key=lambda item: item[1][1])
bed = sorted(bed.items(), key=lambda item: item[1][0], reverse=True)
berries = good + bed
pos = 0
for el in berries:
    res.append(el[0])
    position.append(pos + el[1][0])
    pos = pos + el[1][2]

print(max(position))
print(" ".join(map(str, res)))