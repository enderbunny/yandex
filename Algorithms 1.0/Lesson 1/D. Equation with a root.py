a = int(input())
b = int(input())
c = int(input())

if a == 0 and c >= 0 and c**2 == b:
    print("MANY SOLUTIONS")
elif c < 0 or a == 0: 
    print("NO SOLUTION")
else:
    x = (c**2 - b) / a
    print(f"{x}".rstrip('0').rstrip('.'))