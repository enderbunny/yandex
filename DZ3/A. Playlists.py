n = int(input())

k = int(input())
k_list = input().split()
n -= 1

while n != 0:
    k = int(input())
    k_list = set(k_list) & set(input().split())
    n -= 1

print(len(k_list))
print(' '.join(map(str, sorted(k_list))))
