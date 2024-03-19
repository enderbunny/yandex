def line(n, a):
    new_a = []
    otr = []
    for i in range(n):
        otr.append(a[i])
        if len(otr) == a[i] or len(otr) == min(otr, default=0):
            new_a.append(len(otr))
            otr = []
        elif len(otr) > a[i] or len(otr) > min(otr, default=0):
            otr.pop(-1)
            new_a.append(len(otr))
            otr = [a[i]]
        else:
            if i + 1 == n:
                new_a.append(len(otr))
    print(len(new_a))
    print(' '.join(map(str, new_a)))


t = int(input())
while t != 0:
    line(int(input()), list(map(int, input().split())))
    t -= 1
