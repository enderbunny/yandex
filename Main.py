n, m = map(int, input().split())
a = []
attack = 0
cor = [0, 0]

for i in range(n):
    a.append(list(map(int, input().split())))

print(a)
sumN = list(map(sum, a))
print(sumN)

print(list(zip(*a)))
sumM = list(map(sum, zip(*a)))
print(sumM)

cor[0] = sumN.index(max(sumN)) + 1
cor[1] = sumM.index(max(sumM)) + 1


print(' '.join(map(str, cor)))
