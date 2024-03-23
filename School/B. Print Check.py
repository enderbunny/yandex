str1 = input()
log = input()

i = 0
left, right = '', ''
while i != len(log):
    if log[i:].startswith('<delete>'):
        right = right[1:]
        log = log.replace('<delete>', ' ', 1)
    elif log[i:].startswith('<bspace>'):
        left = left[:-1]
        log = log.replace('<bspace>', ' ', 1)
    elif log[i:].startswith('<left>'):
        if left != '':
            right = left[len(left)-1] + right
            left = left[:-1]
        log = log.replace('<left>', ' ', 1)
    elif log[i:].startswith('<right>'):
        if right != '':
            left = left + right[0]
            right = right[1:]
        log = log.replace('<right>', ' ', 1)
    else:
        left += log[i]
    i += 1

if str1 == left + right:
    print("Yes")
else:
    print("No")
