n = int(input())
summa = 0

while n != 0:
    a = int(input())
    if a % 4 == 3:
        summa += a // 4 + 2
    else:
        summa += a// 4 + a % 4
    n -= 1

print(summa)