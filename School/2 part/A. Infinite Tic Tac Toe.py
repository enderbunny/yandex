def diagonal_left_right(arr, x, y):
    total1 = 1
    total2 = 1
    while (x - (1 * total1), y - (1 * total1)) in arr:
        total1 += 1
    while (x + (1 * total2), y + (1 * total2)) in arr:
        total2 += 1
    return total1 + total2 - 1


def vertical(arr, x, y):
    total1 = 1
    total2 = 1
    while (x - (1 * total1), y) in arr:
        total1 += 1
    while (x + (1 * total2), y) in arr:
        total2 += 1
    return total1 + total2 - 1


def horizontal(arr, x, y):
    total1 = 1
    total2 = 1
    while (x, y - (1 * total1)) in arr:
        total1 += 1
    while (x, y + (1 * total2)) in arr:
        total2 += 1
    return total1 + total2 - 1


def diagonal_right_left(arr, x, y):
    total1 = 1
    total2 = 1
    while (x - (1 * total1), y + (1 * total1)) in arr:
        total1 += 1
    while (x + (1 * total2), y - (1 * total2)) in arr:
        total2 += 1
    return total1 + total2 - 1


n = int(input())
win = 'Draw'

arr_x = set()
arr_o = set()
for i in range(n):
    r, c = map(int, input().split())
    if i % 2 == 0:
        if diagonal_right_left(arr_x, r, c) == 5:
            win = 'First'
        elif diagonal_left_right(arr_x, r, c) == 5:
            win = 'First'
        elif horizontal(arr_x, r, c) == 5:
            win = 'First'
        elif vertical(arr_x, r, c) == 5:
            win = 'First'
        arr_x.add((r, c))
    else:
        if diagonal_right_left(arr_o, r, c) == 5:
            win = 'Second'
        elif diagonal_left_right(arr_o, r, c) == 5:
            win = 'Second'
        elif horizontal(arr_o, r, c) == 5:
            win = 'Second'
        elif vertical(arr_o, r, c) == 5:
            win = 'Second'
        arr_o.add((r, c))
    if win != 'Draw' and i < n-1:
        win = 'Inattention'
        break

print(win)

