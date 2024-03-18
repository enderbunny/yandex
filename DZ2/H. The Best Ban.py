n, m = map(int, input().split())
a = []
cor = [0, 0]

for i in range(n):
    a.append(list(map(int, input().split())))

sumN = list(map(sum, a))
sumM = list(map(sum, zip(*a)))
print(sumN)
print(sumM)

attack = 0

for i in range(len(sumN)):
    for j in range(len(sumM)):
        if sumN[i] + sumM[j] - a[i][j] > attack:
            attack = sumN[i] + sumM[j] - a[i][j]
            cor = [i+1, j+1]

print(' '.join(map(str, cor)))
