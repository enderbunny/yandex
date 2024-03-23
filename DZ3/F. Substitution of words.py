w_list = tuple(input().split())
text = input().split()

for i in range(len(text)):
    print(text)
    for w in w_list:
        if text[i].startswith(w):
            text[i] = w

print(' '.join(map(str, text)))
