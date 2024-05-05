def clear(strok):
    for el in "()+-":
        strok = strok.replace(el, '')
    return strok

def spl(el):
    num = el[-7:]
    reg = el[-10:-7]
    if reg == '':
        reg = '495'    
    return [reg, num]

first = spl(clear(input()))

for i in range(3):
    a = spl(clear(input()))
    if a == first:
        print("YES")
    else:
        print("NO")
