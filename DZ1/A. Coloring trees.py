v = list(map(int, input().split()))
m = list(map(int, input().split()))

at = [v[0] - v[1], v[0] + v[1], m[0] - m[1], m[0] + m[1]]

if (at[0] - at[3]) * (at[2] - at[1]) >= 0:
    print(max(at) - min(at) + 1)
else:
    print(at[1] - at[0] + at[3] - at[2] + 2)