def line(n, a):
    new_a = []
    otr = 1
    min_a = a[0]
    for i in range(n):
        print(a[i], otr, min_a, end='-')
        if min_a > a[i] or otr == 1:
            min_a = a[i]
        print(min_a)
        if otr > a[i] or otr > min_a:
            new_a.append(otr)
            otr = 1
        elif otr == a[i] or otr == min_a:
            new_a.append(otr)
            otr = 1
        else:
            otr += 1

    if otr != 0:
        new_a.append(otr)
    print(len(new_a))
    print(' '.join(map(str, new_a)))


t = int(input())
while t != 0:
    line(int(input()), list(map(int, input().split())))
    t -= 1
