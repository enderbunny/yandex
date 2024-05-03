def line(n, a):
    new_a = []
    otr = []
    for i in range(n):
        otr.append(a[i])
        min_a = min(otr)
        length = len(otr)
        if length > a[i] or length > min_a:
            otr.pop(-1)
            new_a.append(length)
            otr.clear()
            otr.append(a[i])
        elif length == a[i] or length == min_a:
            new_a.append(length)
            otr.clear()

    if len(otr) != 0:
        new_a.append(len(otr))
    print(len(new_a))
    print(' '.join(map(str, new_a)))


t = int(input())
while t != 0:
    line(int(input()), list(map(int, input().split())))
    t -= 1
