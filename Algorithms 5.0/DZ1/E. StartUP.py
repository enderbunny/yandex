i_data = list(map(int, input().split(' ')))\

n = i_data[0]
k = i_data[1]
d = i_data[2]

result = -1
for i in range(10):
    if int(str(n) + str(i)) % k == 0:
        result = i
        break
if result != -1:
    n = str(n) + str(result)
else:
    n = -1
d -= 1

if d != 0 and n != -1:
    n += "0" * d

print(n)