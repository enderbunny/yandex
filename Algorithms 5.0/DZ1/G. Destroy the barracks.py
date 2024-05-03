x = int(input())
y = int(input())
p = int(input())

n = 1
y -= x
p1 = 0

while y > 0:
    p1 += p
    print(x,y,p1)
    if y - x >= 0:
        y -= x
        x -= p1
    else:
        x1 = x - y
        p1 -= x1
        x -= p1
        y = 0
        n += 1
        print(x, y, p1)
        print(n)

while p1 > 0:
    print(x,y,p1)
    if p1 - x > 0:
        print(x, p1)
        p1 -= x
        print(p1)
        x -= p1
        print(x,y,p1)
    else:
        p1 -= x
        n += 1
        print(x,y,p1)
        print(n)

