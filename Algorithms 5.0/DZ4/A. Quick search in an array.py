import bisect

n = int(input())
n_arr = sorted(map(int, input().split()))
res = []
k = int(input())

while k != 0:
    l, r = map(int, input().split())
    lower = bisect.bisect_left(n_arr, l)
    upper = bisect.bisect_right(n_arr, r)
    res.append(upper-lower)
    k -= 1

print(' '.join(map(str, res)))