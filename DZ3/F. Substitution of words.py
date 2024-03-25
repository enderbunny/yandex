w_list = set(input().split())
text = input().split()

res = []
for w in text:
    for i in range(1, len(w)):
        start = w[:i]
        if start in w_list:
            res.append(start)
            break
    else:
        res.append(w)

print(' '.join(map(str, text)))
