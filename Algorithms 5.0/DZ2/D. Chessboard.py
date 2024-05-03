n = int(input())
per = 0
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
cells = []

while n != 0:
    x, y = map(int, input().split())
    j = 0
    for i in range(len(dx)):
        if [x+dx[i], y+dy[i]] in cells:
            j += 1
    cells.append([x, y])
    per += 4 - (2 * j)
    n -= 1

print(per)
