n = int(input())
wheel = list(map(int, input().split()))
a, b, k = map(int, input().split())
win = min(wheel)
i = 0

while a < b + 1 and i != n:
    i += 1
    if a % k == 0:
        step = a // k - 1
    else:
        step = a // k
    if max(wheel[step % n], wheel[-step % n]) > win:
        win = max(wheel[step % n], wheel[-step % n])
    a += k

print(win)
