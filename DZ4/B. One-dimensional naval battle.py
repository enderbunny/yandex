def check(k):
    res = k * k * (k + 1) // 2 - k * (k + 1) * (2 * k + 1) // 6 + k * (k + 1)
    return res <= n + 1


n = int(input())
left = 0
right = n + 1
while right - left > 1:
    middle = (left + right) // 2
    if check(middle):
        left = middle
    else:
        right = middle
print(left)