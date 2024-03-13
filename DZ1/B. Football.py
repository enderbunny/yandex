c1 = list(map(int, input().split(':')))
c2 = list(map(int, input().split(':')))
sum1 = c1[0] + c2[0]
sum2 = c1[1] + c2[1]
ysl = int(input())
res = 0

if ysl == 1:
    if sum1 < sum2:
        res = sum2 - sum1
        if res + c2[0] <= c1[1]:
            res += 1
    elif sum1 == sum2 and c2[0] <= c1[1]:
        res = 1

else:
    if sum1 < sum2:
        res = sum2 - sum1
        if c1[0] <= c2[1]:
            res += 1
    elif sum1 == sum2 and c1[0] <= c2[1]:
        res = 1
print(res)