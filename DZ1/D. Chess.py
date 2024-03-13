B = []
R = []
summa = 0

for i in range(8):
    line = input()
    if 'R' in line:
        R = [i, line.find('R')]
    if 'B' in line:
        B = [i, line.find('B')]

print(R)
print(B)