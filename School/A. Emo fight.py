import re

name = input()
res = 'NO'

a1 = re.search(r'([a-z])+', name)
a2 = re.search(r'([A-Z])+', name)
a3 = re.search(r'\d+', name)

if len(name) >= 8 and a1 is not None and a2 is not None and a3 is not None:
    res = 'YES'

print(res)